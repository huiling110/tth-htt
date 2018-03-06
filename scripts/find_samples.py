#!/usr/bin/env python

import subprocess, re, datetime, collections, jinja2, argparse, os, math, sys, json, itertools, ast, copy

class SmartFormatter(argparse.ArgumentDefaultsHelpFormatter):
  def _split_lines(self, text, width):
    if text.startswith('R|'):
      return text[2:].splitlines()
    return argparse.ArgumentDefaultsHelpFormatter._split_lines(self, text, width)

class Version:
  def __init__(self, version):
    version_split = version.split('_')
    self.major    = int(version_split[0])
    self.minor    = int(version_split[1])
    self.subminor = int(version_split[2])
    self.is_pre_or_patch = 0
    self.pre_or_patch_version = 0

    version_key = 'ver'
    pre_regex = re.compile(r'pre(?P<%s>[0-9]+)' % version_key)
    patch_regex = re.compile(r'patch(?P<%s>[0-9]+)' % version_key)

    if len(version_split) > 3:
      pre_or_patch_str = version_split[3]
      if 'pre' in pre_or_patch_str:
        self.is_pre_or_patch = -1
        pre_match = pre_regex.match(pre_or_patch_str)
        if not pre_match:
          raise ValueError("Unparsable version: '%s'" % version)
        self.pre_or_patch_version = pre_match.group(version_key)
      elif 'patch' in pre_or_patch_str:
        self.is_pre_or_patch = 1
        patch_match = patch_regex.match(pre_or_patch_str)
        if not patch_match:
          raise ValueError("Unparsable version: '%s'" % version)
        self.pre_or_patch_version = patch_match.group('ver')
      else:
        raise ValueError("Unparsable version: '%s'" % version)

  def passes(self, other):
    if self.major >= other.major and self.minor >= other.minor and self.subminor >= other.subminor \
      and self.is_pre_or_patch >= other.is_pre_or_patch:
      if self.is_pre_or_patch == other.is_pre_or_patch:
        return self.pre_or_patch_version >= other.pre_or_patch_version
      return True
    return False

METADICT_HEADER = '''from collections import OrderedDict as OD

# file generated at {{ date }} with the following command:
# {{ command }}

meta_dictionary = OD()

{% if is_mc %}
### event sums

sum_events = { {% for sum_event_arr in sum_events %}
  ("{{ sum_event_arr|join('", "') }}"),
{%- endfor %}
}


{% endif %}
'''

METADICT_TEMPLATE_DATA = '''meta_dictionary["{{ dataset_name }}"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "data_obs"),
  ("process_name_specific", "{{ process_name_specific }}"),
  ("nof_db_events",         {{ nof_db_events }}),
  ("nof_db_files",          {{ nof_db_files }}),
  ("fsize_db",              {{ fsize_db }}),
  ("xsection",              None),
  ("use_it",                True),
  ("genWeight",             False),
  ("run_range",             {{ run_range }}),
  ("golden_run_range",      {{ golden_run_range }}),
  ("comment",               "{{ comment }}"),
])

'''

METADICT_TEMPLATE_MC = '''meta_dictionary["{{ dataset_name }}"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "{{ sample_category }}"),
  ("process_name_specific", "{{ specific_name }}"),
  ("nof_db_events",         {{ nof_db_events }}),
  ("nof_db_files",          {{ nof_db_files }}),
  ("fsize_db",              {{ fsize_db }}),
  ("xsection",              {{ xs }}),
  ("use_it",                {{ use_it }}),
  ("genWeight",             True),
  ("comment",               "{{ comment }}"),
])

'''

DATA_SAMPLES_ALL = [
  'SingleElectron',
  'SingleMuon',
  'DoubleEG',
  'DoubleMuon',
  'MuonEG',
  'Tau',
]
DATA_SAMPLES_DEFAULT = [ data_sample for data_sample in DATA_SAMPLES_ALL if data_sample != 'Tau' ]

DATA_TIER     = 'MINIAOD'
MC_TIER       = '%sSIM' % DATA_TIER
AQC_KEY       = 'cat'
PDS_KEY       = 'data'

DASGOCLIENT_QUERY_COMMON     = "dasgoclient -query='        dataset=%s          | grep dataset.%s' -unique | grep -v '^\\['"
DASGOCLIENT_QUERY_ANY_STATUS = "dasgoclient -query='dataset dataset=%s status=* | grep dataset.%s' -unique | grep -v '^\\['"
DASGOCLIENT_QUERY_RELEASE    = "dasgoclient -query='release dataset=%s' -unique"
DASGOCLIENT_QUERY_RUNLUMI    = "dasgoclient -query='run,lumi dataset=%s' -unique"

MC_REGEX = re.compile(r'/[\w\d_-]+/[\w\d_-]+/%s' % MC_TIER)

def convert_date(date):
  return datetime.datetime.fromtimestamp(int(date)).strftime('%Y-%m-%d %H:%M:%S')

def human_size(fsize, use_si = True, byte_suffix = 'B'):
  if use_si:
    multiplier = 1000.
    units = ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
  else:
    multiplier = 1024.
    units = ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi', 'Yi']
  units = list(map(lambda unit: '%s%s' % (unit, byte_suffix), units))
  fsize_int = int(fsize)
  unit_idx = min(int(math.log(fsize_int, multiplier)), len(units) - 1) if fsize_int else 0
  if unit_idx > 0:
    return '%.2f%s' % ((fsize_int / multiplier ** unit_idx), units[unit_idx])
  else:
    return '%d%s' % (fsize_int, units[unit_idx])

def convert_cmssw_versions(cmssw_list):
  return ','.join(set([
    re.match(r'.*\"(?P<ver>.*)\".*', cmssw_ver).group('ver')[len('CMSSW')+1:]
    for cmssw_ver in cmssw_list.split(',')
  ]))

def id_(x): # identity function
  return x

def run_cmd(cmd_str, return_stderr = True):
  cmd = subprocess.Popen(cmd_str, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
  stdout, stderr = cmd.communicate()
  if return_stderr:
    return stdout, stderr
  return stdout

def get_golden_runlumi(lumimask_location):
  with open(lumimask_location, 'r') as lumimask_file:
    try:
      golden_runlumi_json = json.load(lumimask_file)
    except json.decoder.JSONDecodeError:
      raise ValueError("File %s is not a JSON file" % lumimask_file)
  if not golden_runlumi_json:
    raise ValueError("No JSON-formatted infromation was loaded from %s" % lumimask_file)

  golden_runlumi = collections.OrderedDict(
    (
      int(run),
      list(itertools.chain(*[
        # Expand the luminosity ranges
        # For instance, if the luminosity ranges are
        # [[1, 7], [40, 45]]
        # then this is expanded and flattened into
        # [1, 2, 3, 4, 5, 6, 7, 40, 41, 42, 43, 44, 45]
        # We assume that both endpoints of the luminosity range are included
        list(range(lumi_range[0], lumi_range[-1] + 1)) for lumi_range in lumi_ranges
      ]))
    ) for run, lumi_ranges in golden_runlumi_json.items()
  )
  return golden_runlumi

def get_runlumi_data(runlumi_query_out):
  lines = runlumi_query_out.rstrip('\n').split('\n')
  lines_split = [ line.split() for line in lines ]
  runlumi_data = collections.OrderedDict()
  for line in lines_split:
    run = int(line[0])
    lumis = list(sorted(ast.literal_eval(line[1])))
    runlumi_data[run] = lumis
  return runlumi_data

def get_data_golden(runlumi_data, golden_runlumi):
  data_runs   = set(runlumi_data.keys())
  golden_runs = set(golden_runlumi.keys())
  common_runs = list(sorted(list(data_runs & golden_runs)))

  # We want to check the intersection of each individual common run, because it might be the case
  # that the first or last run do not have any common luminosity blocks and is therefore not
  # part of the golden run. For instance, if a common run, say 304199 has golden range of [10, 18]
  # and the PD also contains run 304199 but only the luminosity blocks [2, 5], then this run should
  # be excluded from the golden runs since there's no overlap in their luminosity range.
  # If such runs happen to be first and/or last in the common runs, then the golden run range will
  # be different from the case where we only find the common run ranges.
  golden_data_runs = collections.OrderedDict()
  for run in common_runs:
    lumi_range_intersection = list(sorted(list(set(runlumi_data[run]) & set(golden_runlumi[run]))))
    if lumi_range_intersection:
      golden_data_runs[run] = copy.deepcopy(lumi_range_intersection)
  return golden_data_runs

if __name__ == '__main__':

  parser = argparse.ArgumentParser(
    formatter_class = lambda prog: SmartFormatter(prog, max_help_position = 55)
  )
  parser.add_argument('-i', '--input',
    type = str, dest = 'input', metavar = 'path', required = False,
    help = 'R|Input file containing MC DBS names (one per line)',
  )
  parser.add_argument('-m', '--metadict',
    type = str, dest = 'metadict', metavar = 'path', default = 'metaDict.py', required = False,
    help = 'R|Output path of the Python meta-dictionary',
  )
  parser.add_argument('-d', '--datasets',
    type = str, dest = 'dataset', metavar = 'path', default = 'datasets.txt', required = False,
    help = 'R|Output path of the dataset list (valid if -i/--input not provided)',
  )
  parser.add_argument('-r', '--run',
    type = str, dest = 'run', metavar = 'run', default = '2017', required = False,
    help = 'R|Data collection period',
  )
  parser.add_argument('-p', '--primary-datasets',
    type = str, nargs = '+', dest = 'primary_datasets', metavar = 'PD', choices = DATA_SAMPLES_ALL,
    default = DATA_SAMPLES_DEFAULT, required = False,
    help = 'R|List of PDs to be considered (choices: %s)' % \
           (', '.join(map(lambda choice: "'%s'" % choice, DATA_SAMPLES_ALL))),
  )
  parser.add_argument('-g', '--golden-json',
    type = str, dest = 'golden_json', metavar = 'file', required = False,
    default = os.path.join(
      os.environ['CMSSW_BASE'], 'src', 'tthAnalysis', 'NanoAOD', 'data',
      'Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'
    ),
    help = 'R|Path to the golden lumimask file in JSON format',
  )
  parser.add_argument('-v', '--cmssw-version',
    type = str, dest = 'version', metavar = 'version', default = '9_4_0', required = False,
    help = 'R|Minimum required CMSSW version',
  )
  parser.add_argument('-V', '--verbose',
    dest = 'verbose', action = 'store_true', default = False, required = False,
    help = 'R|Verbose output',
  )
  args = parser.parse_args()

  has_dasgoclient = run_cmd('which dasgoclient 2>/dev/null | wc -l', False)
  if has_dasgoclient.rstrip('\n') != "1":
    raise ValueError("dasgoclient not available! Set up your 94x environment")
  has_voms_proxy = run_cmd('which voms-proxy-info 2>/dev/null | wc -l', False)
  if has_voms_proxy.rstrip('\n') != "1":
    raise ValueError("voms-proxy-* not available! Set up your 94x environment")

  min_voms_proxy_timeleft_minutes = 30
  voms_proxy_timeleft = int(run_cmd('voms-proxy-info --timeleft', False).rstrip('\n'))
  if voms_proxy_timeleft < 60 * min_voms_proxy_timeleft_minutes:
    raise ValueError(
      "proxy not open at least %i minutes to run this script; "         \
      "update your proxy with: voms-proxy-init -voms cms -valid 1:00" % \
      min_voms_proxy_timeleft_minutes
    )

  mc_input = args.input
  required_cmssw_version_str = args.version
  required_cmssw_version = Version(required_cmssw_version_str)
  verbose = args.verbose

  primary_datasets = args.primary_datasets
  DATA_GREP_STR = '\\|'.join(map(lambda sample: '^/%s/' % sample, primary_datasets))
  DATA_PIPED = '|'.join(primary_datasets)
  MAX_DATA_SAMPLE_LEN = max(map(len, primary_datasets))
  DATA_QUERY = "dasgoclient -query='dataset dataset=/*/*%s*/{data_tier}' | grep '{data_str}' | sort".format(
    data_tier = DATA_TIER,
    data_str  = DATA_GREP_STR,
  )

  lumimask_location = args.golden_json
  if not os.path.isfile(lumimask_location):
    raise ValueError("No such file: %s" % lumimask_location)
  golden_runlumi = get_golden_runlumi(lumimask_location)

  execution_datetime = '{date:%Y-%m-%d %H:%M:%S}'.format(date = datetime.datetime.now())
  execution_command  = ' '.join([os.path.basename(__file__)] + sys.argv[1:])

  if mc_input:
    if not os.path.isfile(mc_input):
      raise ValueError("No such file: %s" % mc_input)

    das_keys = collections.OrderedDict([
      ('name',                   {'colname' : 'Name',            'func' : id_}),
      ('dataset_access_type',    {'colname' : 'Status',          'func' : id_}),
      ('acquisition_era_name',   {'colname' : 'Acq. era name',   'func' : id_}),
      ('primary_ds_type',        {'colname' : 'Primary DS type', 'func' : id_}),
      ('last_modification_date', {'colname' : 'Last modified',   'func' : convert_date}),
      ('size',                   {'colname' : 'Size',            'func' : id_}),
      ('nfiles',                 {'colname' : 'Nof files',       'func' : id_}),
      ('nevents',                {'colname' : 'Nof events',      'func' : id_}),
      ('release',                {'colname' : 'CMSSW release',   'func' : convert_cmssw_versions}),
    ])

    das_query_results = collections.OrderedDict()
    with open(mc_input) as mc_file:
      for line in mc_file:
        line_stripped = line.rstrip('\n')
        field_str = line_stripped.split('#')[0].strip()
        if not field_str:
          # probably a comment or an empty line
          continue
        fields = field_str.split()
        if len(fields) != 4:
          raise ValueError("Unparseable line in file %s: %s" % (line_stripped, mc_input))

        das_name        = fields[0]
        sample_category = fields[1]
        specific_name   = fields[2]
        xs              = float(fields[3]) # let it fail

        if not MC_REGEX.match(das_name):
          raise ValueError("Error: line '%s' does not correspond to proper DBS name" % das_name)
        das_query_results[das_name] = {
          'sample_category' : sample_category,
          'specific_name'   : specific_name,
          'xs'              : xs,
        }

    for dataset_idx, dataset in enumerate(das_query_results):
      if verbose:
        sys.stdout.write(
          "Querying sample (%d/%d): %s;" % (dataset_idx + 1, len(das_query_results), dataset)
        )
      for das_key_idx, das_key in enumerate(das_keys):
        if verbose:
          sys.stdout.write(" %s%s" % (das_key, (',' if das_key_idx != len(das_keys) - 1 else '\n')))
          sys.stdout.flush()
        mc_query_str = DASGOCLIENT_QUERY_COMMON % (dataset, das_key) if das_key != 'release' \
                       else DASGOCLIENT_QUERY_RELEASE % dataset
        mc_query_out, mc_query_err = run_cmd(mc_query_str)
        if not mc_query_out or mc_query_err:
          # this may happen if a sample is in PRODUCTION stage and the dasgoclient script
          # returns nonsense; let's try again with status=*
          query_fail = False
          if das_key != 'release':
            mc_query_str = DASGOCLIENT_QUERY_ANY_STATUS % (dataset, das_key)
            mc_query_out, mc_query_err = run_cmd(mc_query_str)
            if not mc_query_out or mc_query_err:
              query_fail = True
          else:
            query_fail = True
          if query_fail:
            raise ValueError("Query to DAS resulted in an empty output or an error:"
                             "\nstdout = '%s'\nstderr = '%s'" % (mc_query_out, mc_query_err))

        das_parser = das_keys[das_key]['func']
        das_query_results[dataset][das_key] = das_parser(mc_query_out.rstrip('\n')).strip()

    col_widths = {
      das_key:
        max(
          max(
            map(
              lambda col_value: len(col_value), [
                das_query_results[dataset][das_key] for dataset in das_query_results
              ]
            )
          ), len(das_keys[das_key]['colname'])
        ) for das_key in das_keys
    }
    for dataset in das_query_results:
      das_query_results[dataset]['release_pass'] = any(list(map(
        lambda ver: Version(ver).passes(required_cmssw_version),
        das_query_results[dataset]['release'].split(',')
      )))

    print("OK = the sample is produced with CMSSW version %s or greater" % required_cmssw_version_str)
    print(
      ' OK %s' % \
      '  '.join([das_keys[das_key]['colname'].ljust(col_widths[das_key]) for das_key in das_keys])
    )
    for dataset in das_query_results:
      passes_version_req = das_query_results[dataset]['release_pass']
      passes_version_req_tick = 'x' if passes_version_req else ' '
      print('  %s %s' % (
        passes_version_req_tick,
        '  '.join([
          das_query_results[dataset][das_key].ljust(col_widths[das_key]) for das_key in das_keys
        ])
      ))

    meta_dictionary_entries = []
    for dataset in das_query_results:
      entry = das_query_results[dataset]
      meta_dictionary_entries.append(jinja2.Template(METADICT_TEMPLATE_MC).render(
        dataset_name    = entry['name'],
        nof_db_events   = entry['nevents'],
        nof_db_files    = entry['nfiles'],
        fsize_db        = entry['size'],
        sample_category = entry['sample_category'],
        xs              = entry['xs'],
        specific_name   = entry['specific_name'],
        use_it          = entry['dataset_access_type'] != 'INVALID' and entry['release_pass'],
        comment         = "status: %s; size: %s; nevents: %s; release: %s; last modified: %s" % (
          entry['dataset_access_type'],
          human_size(entry['size']),
          human_size(entry['nevents'], use_si = True, byte_suffix = ''),
          entry['release'],
          entry['last_modification_date'],
        ),
      ))

    sum_suffixes = ['_PSweights$', '_ext[1-9]{1}$']
    specific_names = [ dataset_entry['specific_name'] for dataset_entry in das_query_results.values() ]
    sum_events = {}
    for specific_name_ref in specific_names:
      for specific_name_test in specific_names:
        for sum_suffix in sum_suffixes:
          if re.match('^' + specific_name_ref + sum_suffix, specific_name_test):
            if specific_name_ref not in sum_events:
              sum_events[specific_name_ref] = []
            sum_events[specific_name_ref].append(specific_name_test)
    sum_events_flattened = [
      [ specific_name_ref] + specific_name_tests \
      for specific_name_ref, specific_name_tests in sum_events.items()
    ]

    with open(args.metadict, 'w+') as f:
      f.write(jinja2.Template(METADICT_HEADER).render(
        command    = execution_command,
        date       = execution_datetime,
        sum_events = sum_events_flattened,
        is_mc      = True,
      ))
      f.write('\n'.join(meta_dictionary_entries))
      f.write('\n')

  else:
    era = 'Run{year}'.format(year = args.run)
    data_query_str = DATA_QUERY % era
    data_query_out, data_query_err = run_cmd(data_query_str)

    data_samples_list = data_query_out.rstrip('\n').split('\n')
    data_samples_aggr = {data_sample : {} for data_sample in primary_datasets}

    collection_regex = re.compile(r'/(?P<%s>\b(%s)\b)/%s(?P<%s>[A-Z]{1}).+/%s' % \
                                  (PDS_KEY, DATA_PIPED, era, AQC_KEY, DATA_TIER))
    for data_sample in data_samples_list:
      collection_match = collection_regex.match(data_sample)
      if not collection_match:
        raise ValueError("Could not parse sample: %s" % data_sample)
      primary_dataset    = collection_match.group(PDS_KEY)
      aqcuisition_period = collection_match.group(AQC_KEY)

      if primary_dataset not in data_samples_aggr:
        raise ValueError(
          "Data sample '%s' not in any of those: " % (primary_dataset, ', '.join(primary_datasets))
        )
      if aqcuisition_period not in data_samples_aggr[primary_dataset]:
        data_samples_aggr[primary_dataset][aqcuisition_period] = []
      data_samples_aggr[primary_dataset][aqcuisition_period].append(data_sample)

    print(
      "Primary datasets within acquisition era sorted by creation date; "     \
      "V -- produced with CMSSW version %s or later; "                        \
      "L -- latest sample by modification date." % required_cmssw_version_str
    )

    das_keys = collections.OrderedDict([
      ('name',                   {'colname' : 'Name',            'func' : id_}),
      ('dataset_access_type',    {'colname' : 'Status',          'func' : id_}),
      ('acquisition_era_name',   {'colname' : 'Acq. era name',   'func' : id_}),
      ('primary_ds_name',        {'colname' : 'Primary DS name', 'func' : id_}),
      ('primary_ds_type',        {'colname' : 'Primary DS type', 'func' : id_}),
      ('creation_time',          {'colname' : 'Creation time',   'func' : convert_date}),
      ('last_modification_date', {'colname' : 'Last modified',   'func' : convert_date}),
      ('nevents',                {'colname' : 'Nof events',      'func' : id_}),
      ('processing_version',     {'colname' : 'Processing ver.', 'func' : id_}),
      ('size',                   {'colname' : 'Size',            'func' : id_}),
      ('nfiles',                 {'colname' : 'Nof files',       'func' : id_}),
      ('release',                {'colname' : 'CMSSW release',   'func' : convert_cmssw_versions}),
    ])

    data_sample_selection = {}
    for data_sample in primary_datasets:
      if data_sample not in data_samples_aggr:
        continue
      if data_sample not in data_sample_selection:
        data_sample_selection[data_sample] = {}

      for acq_era in sorted(data_samples_aggr[data_sample].keys()):
        if acq_era not in data_sample_selection[data_sample]:
          data_sample_selection[data_sample][acq_era] = None

        datasets = data_samples_aggr[data_sample][acq_era]
        das_query_results = {}
        for dataset in datasets:
          das_query_results[dataset] = {}
          for das_key in das_keys:
            dasgoclient_query = DASGOCLIENT_QUERY_COMMON %                 \
                                (dataset, das_key) if das_key != 'release' \
                                else DASGOCLIENT_QUERY_RELEASE % dataset
            dasgoclient_query_out, dasgoclient_query_err = run_cmd(dasgoclient_query)
            das_parser = das_keys[das_key]['func']
            das_query_results[dataset][das_key] = das_parser(dasgoclient_query_out.rstrip('\n')).strip()

          if das_query_results[dataset]['dataset_access_type'] != 'VALID':
            del das_query_results[dataset]

        col_widths = {
          das_key :
            max(
              max(
                map(
                  lambda col_value: len(col_value), [
                      das_query_results[dataset][das_key] for dataset in das_query_results
                  ]
                )
              ), len(das_keys[das_key]['colname'])
            ) for das_key in das_keys
        }
        for dataset in das_query_results:
          das_query_results[dataset]['release_pass'] = any(list(map(
            lambda ver: Version(ver).passes(required_cmssw_version),
                        das_query_results[dataset]['release'].split(',')
          )))

        sorted_by_creation_time = [
          pair[0] for pair in sorted(
            das_query_results.items(), key = lambda value: value[1]['creation_time']
          )
        ]
        sorted_by_modification_time = [
          pair[0] for pair in sorted(
            das_query_results.items(), key = lambda value: value[1]['last_modification_date']
          )
        ]
        latest_modified_dataset = sorted_by_modification_time[-1]
        nof_passes_cmssw_version = sum([
          int(das_query_results[dataset]['release_pass']) for dataset in das_query_results
        ])

        print(
          'Primary DS name %s, acquisition era %s, found %i datasets, '  \
          '%i of which are produced with CMSSW version %s or greater:' % \
          (data_sample, acq_era, len(das_query_results), nof_passes_cmssw_version, required_cmssw_version_str)
        )
        print(
          ' V L %s' % \
          '  '.join([das_keys[das_key]['colname'].ljust(col_widths[das_key]) for das_key in das_keys])
        )

        selection_list = {}
        for dataset in sorted_by_creation_time:
          is_last_modified   = latest_modified_dataset == dataset
          passes_version_req = das_query_results[dataset]['release_pass']
          is_last_modified_tick   = 'x' if is_last_modified   else ' '
          passes_version_req_tick = 'x' if passes_version_req else ' '
          print(' %s %s %s' % (
            passes_version_req_tick, is_last_modified_tick,
            '  '.join([
              das_query_results[dataset][das_key].ljust(col_widths[das_key]) for das_key in das_keys
            ])
          ))
          if passes_version_req:
            selection_list[dataset] = das_query_results[dataset]

        selection_sorted_by_mod_time = [
          pair[0] for pair in sorted(
            selection_list.items(), key = lambda value: value[1]['last_modification_date']
          )
        ]
        if selection_sorted_by_mod_time:
          selected_dataset = selection_sorted_by_mod_time[-1]
          data_sample_selection[data_sample][acq_era] = selection_list[selected_dataset]

    print("%s\nSummary:" % ('-' * 120))
    meta_dictionary_entries = []
    dataset_list = collections.OrderedDict()
    for dataset in primary_datasets:
      if dataset not in data_sample_selection:
        continue

      for acquisition_era in sorted(data_sample_selection[dataset]):
        selection = data_sample_selection[dataset][acquisition_era]

        if selection:
          # Query the run and luminosity ranges, figure out the golden range (for documentation purposes).
          # Exclude the whole sample if the data sample is not in the golden range.
          # We don't want to query the run and luminosity ranges earlier in the code because we only
          # pick a single sample out of multiple from the same PD & acquisition era combination.
          # Otherwise, we would spend a lot of time on querying and matching the run and luminosity ranges.

          runlumi_query = DASGOCLIENT_QUERY_RUNLUMI % selection['name']
          runlumi_query_out, runlumi_query_err = run_cmd(runlumi_query)
          if not runlumi_query_out or runlumi_query_err:
            raise ValueError(
              "Was not able to fetch run and lumi ranges for the sample: %s" % selection['name']
            )

          runlumi_data = get_runlumi_data(runlumi_query_out)
          runlumi_data_golden = get_data_golden(runlumi_data, golden_runlumi)

          if runlumi_data_golden:
            # Let's find the min/max (golden) run ranges
            minmax_runlumi_data        = [ min(runlumi_data.keys()), max(runlumi_data.keys())               ]
            minmax_runlumi_data_golden = [ min(runlumi_data_golden.keys()), max(runlumi_data_golden.keys()) ]

            print('  %s, %s%s -> %s' % (dataset.rjust(MAX_DATA_SAMPLE_LEN), era, acquisition_era, selection['name']))
            meta_dictionary_entries.append(jinja2.Template(METADICT_TEMPLATE_DATA).render(
              dataset_name          = selection['name'],
              process_name_specific = '_'.join(selection['name'].split('/')[1:-1]).replace('-', '_'),
              nof_db_events         = selection['nevents'],
              nof_db_files          = selection['nfiles'],
              fsize_db              = selection['size'],
              run_range             = minmax_runlumi_data,
              golden_run_range      = minmax_runlumi_data_golden,
              comment               = "status: %s; size: %s; nevents: %s; release: %s; last modified: %s" % (
                selection['dataset_access_type'],
                human_size(selection['size']),
                human_size(selection['nevents'], use_si = True, byte_suffix = ''),
                selection['release'],
                selection['last_modification_date'],
              ),
            ))
            dataset_list[selection['name']] = {
              'run_range'        : '%d-%d' % tuple(minmax_runlumi_data),
              'golden_run_range' : '%d-%d' % tuple(minmax_runlumi_data_golden),
            }
          else:
            print(
              '  %s, %s%s -> excluded only because no golden run range' % \
              (dataset.rjust(MAX_DATA_SAMPLE_LEN), era, acquisition_era)
            )
        else:
          print('  %s, %s%s -> missing' % (dataset.rjust(MAX_DATA_SAMPLE_LEN), era, acquisition_era))

    with open(args.metadict, 'w+') as f:
      f.write(jinja2.Template(METADICT_HEADER).render(
        command = execution_command,
        date    = execution_datetime,
        is_mc   = False,
      ))
      f.write('\n'.join(meta_dictionary_entries))
      f.write('\n')

    with open(args.dataset, 'w+') as f:
      max_dataset_name_len     = max(map(len, dataset_list.keys()))
      max_run_range_len        = max(map(lambda d: len(d['run_range']),        dataset_list.values()))
      max_golden_run_range_len = max(map(lambda d: len(d['golden_run_range']), dataset_list.values()))
      dataset_format = "%s   %s   %s\n"
      f.write(
        dataset_format % \
        (
          "# DAS name".ljust(max_dataset_name_len),
          "run range".ljust(max_run_range_len),
          "golden run range".ljust(max_golden_run_range_len),
        )
      )
      for dataset_name, run_dict in dataset_list.items():
        f.write(
          dataset_format % \
          (
            dataset_name.ljust(max_dataset_name_len),
            run_dict['run_range'].ljust(max_run_range_len),
            run_dict['golden_run_range'].ljust(max_golden_run_range_len),
          )
        )
      f.write(
        "\n# file generated at %s with the following command:\n# %s\n" % \
        (execution_datetime, execution_command)
      )
