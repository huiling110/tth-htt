#!/usr/bin/env python
import os, logging, sys, getpass
from tthAnalysis.HiggsToTauTau.configs.analyzeConfig_3l_1tau import analyzeConfig_3l_1tau
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples

# E.g.: ./tthAnalyzeRun_3l_1tau.py -v 2017Dec13 -m default -e 2017

mode_choices         = [
  'default', 'addMEM', 'forBDTtraining_beforeAddMEM', 'forBDTtraining_afterAddMEM', 'sync', 'sync_wMEM'
]
sys_choices      = [ 'full' ] + systematics.an_extended_opts
systematics.full = systematics.an_extended

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_preselect()
parser.add_rle_select()
parser.add_nonnominal()
parser.add_tau_id_wp()
parser.add_hlt_filter()
parser.add_files_per_job()
parser.add_use_home()
parser.add_lep_mva_wp()
#parser.add_lep_minPt_lead()
#parser.add_lep_minPt_sublead()
#parser.add_lep_minPt_third()
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
lep_mva_wp        = args.lep_mva_wp
#lep_minPt_lead    = args.lep_minPt_lead
#lep_minPt_sublead = args.lep_minPt_sublead
#lep_minPt_third   = args.lep_minPt_third
lep_minPt_lead    = 20. # current default values of 3l+1tau channel
lep_minPt_sublead = 10.
lep_minPt_third   = 10.
#lep_minPt_lead    = 25. # current default values of 3l channel
#lep_minPt_sublead = 15.
#lep_minPt_third   = 10.

# 20/10/10 per AN2016_372_v14:360, but 25/15 if e (10 if mu)/10 in the old VHbb branch

# Use the arguments
central_or_shifts = []
for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)
do_sync = mode.startswith('sync')
lumi = get_lumi(era)

MEMbranch           = ''
chargeSumSelections = [ "OS" ] if "forBDTtraining" in mode else [ "OS", "SS" ]

if mode == "default":
  if use_preselected:
    if era == "2016":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2016_preselected import samples_2016 as samples
    elif era == "2017":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017_preselected import samples_2017 as samples
    elif era == "2019":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2018_preselected import samples_2018 as samples
    else:
      raise ValueError("Invalid era: %s" % era)
  else:
    if era == "2016":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2016 import samples_2016 as samples
    elif era == "2017":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017 import samples_2017 as samples
    elif era == "2018":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2018 import samples_2018 as samples
    else:
      raise ValueError("Invalid era: %s" % era)

  if era == "2016":
    hadTau_selection = "dR03mvaMedium"
  elif era == "2017":
    hadTau_selection = "dR03mvaLoose"
  elif era == "2018":
    raise ValueError("Implement me!")
  else:
    raise ValueError("Invalid era: %s" % era)

  applyFakeRateWeights = "3lepton"
elif mode == "addMEM":
  if use_preselected:
    if era == "2016":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2016_addMEM_preselected_3l1tau import samples_2016 as samples
    elif era == "2017":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017_addMEM_preselected_3l1tau import samples_2017 as samples
    elif era == "2018":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2018_addMEM_preselected_3l1tau import samples_2018 as samples
    else:
      raise ValueError("Invalid era: %s" % era)
  else:
    if era == "2016":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2016_addMEM_3l1tau import samples_2016 as samples
    elif era == "2017":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017_addMEM_3l1tau import samples_2017 as samples
    elif era == "2018":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2018_addMEM_3l1tau import samples_2018 as samples
    else:
      raise ValueError("Invalid era: %s" % era)

  if era == "2016":
    MEMbranch        = 'memObjects_3l_1tau_lepFakeable_tauTight_dR03mvaVLoose'
    hadTau_selection = "dR03mvaVLoose"
  elif era == "2017":
    MEMbranch        = 'memObjects_3l_1tau_lepFakeable_tauTight_dR03mvaLoose'
    hadTau_selection = "dR03mvaLoose"
  elif era == "2018":
    raise ValueError("Implement me!")
  else:
    raise ValueError("Invalid era: %s" % era)

  applyFakeRateWeights = "3lepton"
elif mode == "forBDTtraining_beforeAddMEM":
  if use_preselected:
    raise ValueError("Makes no sense to use preselected samples w/ BDT training mode")
  else:
    if era == "2016":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2016_BDT import samples_2016 as samples
    elif era == "2017":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017_BDT import samples_2017 as samples
    elif era == "2018":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2018_BDT import samples_2018 as samples
    else:
      raise ValueError("Invalid era: %s" % era)

  if era == "2016":
    hadTau_selection         = "dR03mvaTight"
    hadTau_selection_relaxed = "dR03mvaVVLoose"
  elif era == "2017":
    hadTau_selection         = "dR03mvaTight"
    hadTau_selection_relaxed = "dR03mvaVVLoose"
  elif era == "2018":
    raise ValueError("Implement me!")
  else:
    raise ValueError("Invalid era: %s" % era)

  applyFakeRateWeights = "4L"
elif mode == "forBDTtraining_afterAddMEM":
  if use_preselected:
    raise ValueError("Makes no sense to use preselected samples w/ BDT training mode")
  else:
    if era == "2016":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2016_BDT_addMEM_3l1tau import samples_2016 as samples
    elif era == "2017":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017_BDT_addMEM_3l1tau import samples_2017 as samples
    elif era == "2018":
      from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2018_BDT_addMEM_3l1tau import samples_2018 as samples
    else:
      raise ValueError("Invalid era: %s" % era)

  if era == "2016":
    MEMbranch                = 'memObjects_3l_1tau_lepLoose_tauTight_dR03mvaVLoose'
    hadTau_selection         = "dR03mvaVTight"
    hadTau_selection_relaxed = "dR03mvaVLoose"
  elif era == "2017":
    MEMbranch                = 'memObjects_3l_1tau_lepLoose_tauTight_dR03mvaVVLoose'
    hadTau_selection         = "dR03mvaTight"
    hadTau_selection_relaxed = "dR03mvaVVLoose"
  elif era == "2018":
    raise ValueError("Implement me!")
  else:
    raise ValueError("Invalid era: %s" % era)

  applyFakeRateWeights     = "4L"
elif mode.startswith("sync"):
  if mode == "sync_wMEM":
    if use_preselected:
      if era == "2016":
        from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2016_addMEM_preselected_sync import samples_2016 as samples
      elif era == "2017":
        from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017_addMEM_preselected_sync import samples_2017 as samples
      elif era == "2018":
        from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2018_addMEM_preselected_sync import samples_2018 as samples
      else:
        raise ValueError("Invalid era: %s" % era)
    else:
      if era == "2016":
        from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2016_addMEM_sync import samples_2016 as samples
      elif era == "2017":
        from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017_addMEM_sync import samples_2017 as samples
      elif era == "2018":
        from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2018_addMEM_sync import samples_2018 as samples
      else:
        raise ValueError("Invalid era: %s" % era)
  elif mode == "sync":
    if use_preselected:
      if era == "2016":
        from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2016_preselected_sync import samples_2016 as samples
      elif era == "2017":
        from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017_preselected_sync import samples_2017 as samples
      elif era == "2018":
        from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2018_preselected_sync import samples_2018 as samples
      else:
        raise ValueError("Invalid era: %s" % era)
    else:
      if use_nonnominal:
        if era == "2016":
          from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2016_sync import samples_2016 as samples
        elif era == "2017":
          from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017_sync import samples_2017 as samples
        elif era == "2018":
          from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2018_sync import samples_2018 as samples
        else:
          raise ValueError("Invalid era: %s" % era)
      else:
        if era == "2016":
          from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2016_sync_nom import samples_2016 as samples
        elif era == "2017":
          from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017_sync_nom import samples_2017 as samples
        elif era == "2018":
          from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2018_sync_nom import samples_2018 as samples
        else:
          raise ValueError("Invalid era: %s" % era)
  else:
    raise ValueError("Invalid mode: %s" % mode)

  if era == "2016":
    hadTau_selection = "dR03mvaMedium"
  elif era == "2017":
    hadTau_selection = "dR03mvaLoose"
  elif era == "2018":
    raise ValueError("Implement me!")
  else:
    raise ValueError("Invalid era: %s" % era)
  applyFakeRateWeights = "3lepton"
else:
  raise ValueError("Invalid mode: %s" % mode)

if __name__ == '__main__':
  logging.basicConfig(
    stream = sys.stdout,
    level  = logging.INFO,
    format = '%(asctime)s - %(levelname)s: %(message)s',
  )

  logging.info(
    "Running the jobs with the following systematic uncertainties enabled: %s" % \
    ', '.join(central_or_shifts)
  )
  if not use_preselected:
    logging.warning('Running the analysis on fully inclusive samples!')

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  if args.tau_id_wp:
    logging.info("Changing tau ID working point: %s -> %s" % (hadTau_selection, args.tau_id_wp))
    hadTau_selection = args.tau_id_wp

  analysis = analyzeConfig_3l_1tau(
    configDir = os.path.join("/home",       getpass.getuser(), "ttHAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "ttHAnalysis", era, version),
    executable_analyze                    = "analyze_3l_1tau",
    cfgFile_analyze                       = "analyze_3l_1tau_cfg.py",
    samples                               = samples,
    MEMbranch                             = MEMbranch,
    lep_mva_wp                            = lep_mva_wp,
    lep_minPt_lead                        = lep_minPt_lead,
    lep_minPt_sublead                     = lep_minPt_sublead,
    lep_minPt_third                       = lep_minPt_third,
    hadTau_selection                      = hadTau_selection,
    # CV: apply "fake" background estimation to leptons only and not to hadronic taus, as discussed on slide 10 of
    #     https://indico.cern.ch/event/597028/contributions/2413742/attachments/1391684/2120220/16.12.22_ttH_Htautau_-_Review_of_systematics.pdf
    applyFakeRateWeights                  = applyFakeRateWeights,
    chargeSumSelections                   = chargeSumSelections,
    central_or_shifts                     = central_or_shifts,
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
      "EventCounter"                     : {},
      "numJets"                          : {},
      "mvaDiscr_3l"                      : {},
      "mTauTauVis"                       : {},
      "mvaOutput_plainKin_tt"            : { 'quantile_rebin' : 6, 'quantile_in_fakes' : False }, # BDT2; quantile in all bkg
      "mvaOutput_plainKin_ttV"           : { 'quantile_rebin' : 6, 'quantile_in_fakes' : False }, # BDT1; quantile in all bkg
      "mvaOutput_plainKin_SUM_M"         : { 'explicit_binning' : [ 0.0, 0.28, 0.35, 0.40, 0.47, 0.53, 1.0 ] }, # BDT3; quantile in all bkg
      "mvaOutput_plainKin_SUM_M_noRebin" : {},
      "mvaOutput_plainKin_1B_M"          : {},
      "mvaOutput_final"                  : {},
    },
    select_rle_output                     = True,
    select_root_output                    = False,
    dry_run                               = dry_run,
    do_sync                               = do_sync,
    isDebug                               = debug,
    rle_select                            = rle_select,
    use_nonnominal                        = use_nonnominal,
    hlt_filter                            = hlt_filter,
    use_home                              = use_home,
  )

  if mode.find("forBDTtraining") != -1:
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
