#!/usr/bin/env python

from tthAnalysis.HiggsToTauTau.configs.analyzeConfig_0l_2tau import analyzeConfig_0l_2tau
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples

import os
import sys
import getpass
import re

# E.g.: ./test/tthAnalyzeRun_0l_2tau.py -v 2017Dec13 -m default -e 2017

mode_choices     = [ 'default', 'forBDTtraining', 'sync' ]
sys_choices      = [ 'full' ] + systematics.an_common_opts + [ 'topPtReweighting' ]
systematics.full = systematics.an_common + systematics.topPtReweighting

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_preselect()
parser.add_rle_select()
parser.add_nonnominal()
parser.add_tau_id_wp()
parser.add_tau_id()
parser.add_hlt_filter()
parser.add_files_per_job()
parser.add_use_home()
parser.add_jet_cleaning()
parser.add_gen_matching()
parser.add_sideband()
parser.do_MC_only()
args = parser.parse_args()

# Common arguments
era                = args.era
version            = args.version
dry_run            = args.dry_run
no_exec            = args.no_exec
auto_exec          = args.auto_exec
check_output_files = not args.not_check_input_files
debug              = args.debug
sample_filter      = args.filter
num_parallel_jobs  = args.num_parallel_jobs
running_method     = args.running_method

# Additional arguments
mode              = args.mode
systematics_label = args.systematics
use_preselected   = args.use_preselected
rle_select        = os.path.expanduser(args.rle_select)
use_nonnominal    = args.original_central
hlt_filter        = args.hlt_filter
files_per_job     = args.files_per_job
use_home          = args.use_home
jet_cleaning      = args.jet_cleaning
gen_matching      = args.gen_matching
sideband          = args.sideband
tau_id            = args.tau_id
MC_only           = args.MC_only

# Use the arguments
central_or_shifts = []
for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)
do_sync = mode.startswith('sync')
lumi = get_lumi(era)
jet_cleaning_by_index = (jet_cleaning == 'by_index')
gen_matching_by_index = (gen_matching == 'by_index')

hadTauWP_map = {
  'dR03mva' : 'Medium',
  'deepVSj' : 'Loose', # 'Medium' #
}
hadTau_selection = tau_id + hadTauWP_map[tau_id]

if sideband == 'disabled':
  hadTau_charge_selections = [ "OS" ]
elif sideband == 'enabled':
  hadTau_charge_selections = [ "OS", "SS" ]
elif sideband == 'only':
  hadTau_charge_selections = [ "SS" ]
else:
  raise ValueError("Invalid choice for the sideband: %s" % sideband)

if mode == "default":
  samples = load_samples(era, suffix = "preselected" if use_preselected else "")
  for sample_name, sample_info in samples.items():
    if sample_name == 'sum_events':
      continue
    if sample_info["process_name_specific"].startswith("DYBBJetsToLL_M-50"):
      sample_info["use_it"] = True
elif mode == "forBDTtraining":
  if use_preselected:
    raise ValueError("Makes no sense to use preselected samples w/ BDT training mode")
  samples = load_samples(era, suffix = "BDT_DY")
  hadTauWP_map_relaxed = {
    'dR03mva' : 'VLoose',
    'deepVSj' : 'Loose',
  }
  if args.tau_id_wp:
    tau_id = args.tau_id[:7]
  hadTau_selection_relaxed = tau_id + hadTauWP_map_relaxed[tau_id]
elif mode == "sync":
  sample_suffix = "sync" if use_nonnominal else "sync_nom"
  if use_preselected:
    sample_suffix = "preselected_{}".format(sample_suffix)
  samples = load_samples(era, suffix = sample_suffix)
else:
  raise ValueError("Invalid mode: %s" % mode)

evtCategories = None
if mode == "default" and len(central_or_shifts) <= 1:
  evtCategories = [
    "0l_2tau_0bM_2j", "0l_2tau_1bM_2j", "0l_2tau_2bM_2j",
  ]
else:
  evtCategories = []

for sample_name, sample_info in samples.items():
  if sample_name == 'sum_events':
    continue
  if sample_info["type"] == "mc":
    sample_info["triggers"] = [ "2tau" ]
  if sample_info["type"] == "data":
    sample_info["use_it"] = sample_name.startswith("/Tau/") and mode == "default"
  elif re.match("/DY(\d)?Jets", sample_name):
    sample_info["sample_category"] = "DY"
  elif sample_name.startswith('/TTJets'):
    sample_info["use_it"] = mode == "forBDTtraining"
    sample_info["sample_category"] = "TT"
  elif sample_name.startswith('/TTTo'):
    sample_info["use_it"] = mode == "default"
    sample_info["sample_category"] = "TT"
    sample_info["apply_toppt_rwgt"] = True
  if MC_only :
    if sample_info["type"] == "data" :
      sample_info["use_it"] = False

if __name__ == '__main__':
  logging.info(
    "Running the jobs with the following systematic uncertainties enabled: %s" % \
    ', '.join(central_or_shifts)
  )

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  if args.tau_id_wp:
    logging.info("Changing tau ID working point: %s -> %s" % (hadTau_selection, args.tau_id_wp))
    hadTau_selection = args.tau_id_wp

  analysis = analyzeConfig_0l_2tau(
    configDir = os.path.join("/home",       getpass.getuser(), "ttHAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "ttHAnalysis", era, version),
    executable_analyze                    = "analyze_0l_2tau",
    cfgFile_analyze                       = "analyze_0l_2tau_cfg.py",
    samples                               = samples,
    hadTau_selection                      = hadTau_selection,
    hadTau_charge_selections              = hadTau_charge_selections,
    applyFakeRateWeights                  = "2tau",
    jet_cleaning_by_index                 = jet_cleaning_by_index,
    gen_matching_by_index                 = gen_matching_by_index,
    central_or_shifts                     = central_or_shifts,
    evtCategories                         = evtCategories,
    max_files_per_job                     = files_per_job,
    era                                   = era,
    use_lumi                              = True,
    lumi                                  = lumi,
    check_output_files                    = check_output_files,
    running_method                        = running_method,
    num_parallel_jobs                     = num_parallel_jobs,
    executable_addBackgrounds             = "addBackgrounds",
    # CV: use common executable for estimating jet->lepton and jet->tau_h fake background
    executable_addBackgroundJetToTauFakes = "addBackgroundLeptonFakes",
    histograms_to_fit                     = {
      "EventCounter"                 : {},
      "numJets"                      : {},
      "mvaOutput_Legacy"             : {},
      "mva_Updated"                  : {},
      "mTauTauVis"                   : {},
      "mTauTau"                      : {},
    },
    select_rle_output                     = True,
    dry_run                               = dry_run,
    do_sync                               = do_sync,
    isDebug                               = debug,
    rle_select                            = rle_select,
    use_nonnominal                        = use_nonnominal,
    hlt_filter                            = hlt_filter,
    use_home                              = use_home,
  )

  if mode == "forBDTtraining" :
    analysis.set_BDT_training(hadTau_selection_relaxed)

  job_statistics = analysis.create()
  for job_type, num_jobs in job_statistics.items():
    logging.info(" #jobs of type '%s' = %i" % (job_type, num_jobs))

  if auto_exec:
    run_analysis = True
  elif no_exec:
    run_analysis = False
  else:
    run_analysis = query_yes_no("Start jobs ?")
  if run_analysis:
    analysis.run()
  else:
    sys.exit(0)
