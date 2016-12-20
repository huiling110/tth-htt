import logging

from tthAnalysis.HiggsToTauTau.analyzeConfig import *
from tthAnalysis.HiggsToTauTau.jobTools import create_if_not_exists
from tthAnalysis.HiggsToTauTau.analysisTools import initDict, getKey, create_cfg, createFile, generateInputFileList

def get_lepton_and_hadTau_selection_and_frWeight(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight):
  lepton_and_hadTau_selection_and_frWeight = lepton_and_hadTau_selection
  if lepton_and_hadTau_selection.startswith("Fakeable"):
    if lepton_and_hadTau_frWeight == "enabled":
      lepton_and_hadTau_selection_and_frWeight += "_wFakeRateWeights"
    elif lepton_and_hadTau_frWeight == "disabled":
      lepton_and_hadTau_selection_and_frWeight += "_woFakeRateWeights"
  lepton_and_hadTau_selection_and_frWeight = lepton_and_hadTau_selection_and_frWeight.replace("|", "_")    
  return lepton_and_hadTau_selection_and_frWeight

def getHistogramDir(lepton_selection, lepton_frWeight, lepton_charge_selection):
  histogramDir = "2lss_1tau_%s_%s" % (lepton_charge_selection, lepton_selection)
  if lepton_selection.find("Fakeable") != -1:
    if lepton_frWeight == "enabled":
      histogramDir += "_wFakeRateWeights"
    elif lepton_frWeight == "disabled":
      histogramDir += "_woFakeRateWeights"
  return histogramDir

class analyzeConfig_2lss_1tau(analyzeConfig):
  """Configuration metadata needed to run analysis in a single go.
  
  Sets up a folder structure by defining full path names; no directory creation is delegated here.
  
  Args specific to analyzeConfig_2lss_1tau:
    lepton_selections: either `Tight`, `Loose` or `Fakeable`
    hadTau_selection: either `dR05isoLoose/Medium/Tight` or `dR03mvaMedium/Tight/VTight/VVTight`

  See $CMSSW_BASE/src/tthAnalysis/HiggsToTauTau/python/analyzeConfig.py
  for documentation of further Args.
  
  """
  def __init__(self, outputDir, executable_analyze, cfgFile_analyze_original, samples, lepton_charge_selections, hadTau_selection, applyFakeRateWeights, central_or_shifts,
               max_files_per_job, era, use_lumi, lumi, debug, running_method, num_parallel_jobs, 
               executable_addBackgrounds, executable_addFakes, executable_addFlips, histograms_to_fit, select_rle_output = False, executable_prep_dcard="prepareDatacard"):
    analyzeConfig.__init__(self, outputDir, executable_analyze, "2lss_1tau", central_or_shifts,
      max_files_per_job, era, use_lumi, lumi, debug, running_method, num_parallel_jobs, 
      histograms_to_fit)

    self.samples = samples

    self.lepton_and_hadTau_selections = [ "Tight", "Fakeable", "Fakeable_mcClosure" ]
    self.lepton_and_hadTau_frWeights = [ "enabled", "disabled" ]
    self.lepton_charge_selections = lepton_charge_selections
    self.hadTau_selection_part2 = hadTau_selection
    self.applyFakeRateWeights = applyFakeRateWeights
        
    self.lepton_genMatches = [ "2l0j", "1l1j", "0l2j" ]
    self.hadTau_genMatches = [ "1t0e0m0j", "0t1e0m0j", "0t0e1m0j", "0t0e0m1j" ]

    self.apply_leptonGenMatching = None
    self.apply_hadTauGenMatching = None
    self.lepton_and_hadTau_genMatches_nonfakes = []
    self.lepton_and_hadTau_genMatches_fakes = []
    if self.applyFakeRateWeights == "3L":
      self.apply_leptonGenMatching = True
      self.apply_hadTauGenMatching = True
      for lepton_genMatch in self.lepton_genMatches:
        for hadTau_genMatch in self.hadTau_genMatches:
          lepton_and_hadTau_genMatch = "&".join([ lepton_genMatch, hadTau_genMatch ])
          if lepton_genMatch.endswith("0j") and hadTau_genMatch.endswith("0j"):
            self.lepton_and_hadTau_genMatches_nonfakes.append(lepton_and_hadTau_genMatch)
          else:
            self.lepton_and_hadTau_genMatches_fakes.append(lepton_and_hadTau_genMatch)
    elif applyFakeRateWeights == "2lepton":
      self.apply_leptonGenMatching = True
      self.apply_hadTauGenMatching = False
      for lepton_genMatch in self.lepton_genMatches:
        if lepton_genMatch.endswith("0j"):
          self.lepton_and_hadTau_genMatches_nonfakes.append(lepton_genMatch)
        else:
          self.lepton_and_hadTau_genMatches_fakes.append(lepton_genMatch)
    else:
      raise ValueError("Invalid Configuration parameter 'applyFakeRateWeights' = %s !!" % applyFakeRateWeights)

    self.executable_addBackgrounds = executable_addBackgrounds    
    self.executable_addFakes = executable_addFakes
    self.executable_addFlips = executable_addFlips
    
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"] or sample_info["sample_category"] in [ "additional_signal_overlap", "background_data_estimate" ]:
        continue
      process_name = sample_info["process_name_specific"]
      for lepton_and_hadTau_selection in self.lepton_and_hadTau_selections:
        for lepton_and_hadTau_frWeight in self.lepton_and_hadTau_frWeights:
          if lepton_and_hadTau_frWeight == "enabled" and not lepton_and_hadTau_selection.startswith("Fakeable"):
            continue
          lepton_and_hadTau_selection_and_frWeight = get_lepton_and_hadTau_selection_and_frWeight(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight)
          for lepton_charge_selection in self.lepton_charge_selections:
            key_dir = getKey(sample_name, lepton_and_hadTau_selection, lepton_and_hadTau_frWeight, lepton_charge_selection)
            for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS, DKEY_RLES ]:
              initDict(self.dirs, [ key_dir, dir_type ])
              self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel,
                "_".join([ lepton_and_hadTau_selection_and_frWeight, lepton_charge_selection ]), process_name)
    for dir_type in [ DKEY_DCRD, DKEY_PLOT ]:
      initDict(self.dirs, [ dir_type ])
      self.dirs[dir_type] = os.path.join(self.outputDir, dir_type, self.channel)
    ##print "self.dirs = ", self.dirs

    if self.applyFakeRateWeights == "3L":
      self.nonfake_backgrounds = [ "TT", "TTW", "TTZ", "EWK", "Rares" ]
      self.prep_dcard_processesToCopy = [ "data_obs", "TT", "TTW", "TTZ", "EWK", "Rares", "fakes_data", "fakes_mc", "flips_data" ]
      self.make_plots_backgrounds = [ "TT", "TTW", "TTZ", "EWK", "Rares", "fakes_data", "flips_data" ]
    elif applyFakeRateWeights == "2lepton":
      if era == '2015':
        for sample_name in [
          "/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v2/MINIAODSIM",
          "/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM",
          "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM",
          "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM",
          "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM",
          "/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM",
          "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM",
          "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM",
          "/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM",
          "/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/MINIAODSIM",
          "/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v2/MINIAODSIM",
          "/WWTo2L2Nu_13TeV-powheg/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM",
          "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM" ]:
          self.samples[sample_name]["sample_category"] = "background_data_estimate"
        self.samples["/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM"]["sample_category"] = "WZ"        
      elif era == '2016':
        for sample_name in [ 
          '/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',
          '/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM',
          '/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',
          '/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM',
          '/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v4/MINIAODSIM',
          '/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM',
          '/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',
          '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/MINIAODSIM',
          '/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/MINIAODSIM',
          '/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',
          '/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',
          '/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',
          '/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',
          '/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',
          '/WWTo2L2Nu_13TeV-powheg/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',
          '/ZZTo4L_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM' ]:
          self.samples[sample_name]["sample_category"] = "background_data_estimate"
        self.samples["/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM"]["sample_category"] = "WZ"
      else:
        raise ValueError("Invalid Configuration parameter 'era' = %s !!" % era)
      self.nonfake_backgrounds = [ "TTW", "TTZ", "WZ", "Rares" ]
      self.prep_dcard_processesToCopy = [ "data_obs", "TTW", "TTZ", "WZ", "Rares", "fakes_data", "fakes_mc", "flips_data" ]
      self.make_plots_backgrounds = [ "TTW", "TTZ", "WZ", "Rares", "fakes_data", "flips_data" ]
    else:
      raise ValueError("Invalid Configuration parameter 'applyFakeRateWeights' = %s !!" % applyFakeRateWeights)
      
    self.cfgFile_analyze_original = os.path.join(self.workingDir, cfgFile_analyze_original)
    self.cfgFile_addBackgrounds_original = os.path.join(self.workingDir, "addBackgrounds_cfg.py")
    self.cfgFile_addBackgrounds_modified = {}
    self.histogramFile_addBackgrounds = {}
    self.histogramDir_addBackgrounds = {}    
    self.process_output_addBackgrounds = {}            
    self.histogramFile_hadd_stage1_5 = os.path.join(self.outputDir, DKEY_HIST, "histograms_harvested_stage1_5_%s.root" % self.channel)
    self.cfgFile_addFakes_original = os.path.join(self.workingDir, "addBackgroundLeptonFakes_cfg.py")
    self.cfgFile_addFakes_modified = {}
    self.histogramFile_addFakes = {}
    self.histogramFile_addFlips = os.path.join(self.outputDir, DKEY_HIST, "addBackgroundLeptonFlips_%s.root" % self.channel)
    self.cfgFile_addFlips_original = os.path.join(self.workingDir, "addBackgroundLeptonFlips_cfg.py")
    self.cfgFile_addFlips_modified = os.path.join(self.outputDir, DKEY_CFGS, "addBackgroundLeptonFlips_%s_cfg.py" % self.channel)
    self.histogramDir_prep_dcard = "2lss_1tau_SS_Tight"
    self.histogramDir_prep_dcard_OS = "2lss_1tau_OS_Tight"
    self.cfgFile_make_plots_original = os.path.join(self.workingDir, "makePlots_2lss_1tau_cfg.py")
    self.cfgFile_make_plots_mcClosure_original = os.path.join(self.workingDir, "makePlots_mcClosure_cfg.py")
    self.cfgFiles_make_plots_mcClosure_modified = []

    self.select_rle_output = select_rle_output
    
  def createCfg_analyze(self, inputFiles, outputFile, sample_category, era, triggers,
                        lepton_selection, apply_leptonGenMatching, lepton_charge_selection, hadTau_selection, apply_hadTauGenMatching,
                        applyFakeRateWeights, is_mc, central_or_shift, lumi_scale, apply_genWeight, apply_trigger_bits, cfgFile_modified, rle_output_file):
    """Create python configuration file for the analyze_2lss_1tau executable (analysis code)

    Args:
      inputFiles: list of input files (Ntuples)
      outputFile: output file of the job -- a ROOT file containing histogram
      process: either `TTW`, `TTZ`, `Rares`, `data_obs`, `ttH_hww`, `ttH_hzz` or `ttH_htt`
      is_mc: flag indicating whether job runs on MC (True) or data (False)
      lumi_scale: event weight (= xsection * luminosity / number of events)
      central_or_shift: either 'central' or one of the systematic uncertainties defined in $CMSSW_BASE/src/tthAnalysis/HiggsToTauTau/bin/analyze_2lss_1tau.cc
    """  
    lines = []
    ##lines.append("process.fwliteInput.fileNames = cms.vstring(%s)" % [ os.path.basename(inputFile) for inputFile in inputFiles ])
    lines.append("process.fwliteInput.fileNames = cms.vstring(%s)" % inputFiles)
    lines.append("process.fwliteOutput.fileName = cms.string('%s')" % os.path.basename(outputFile))
    lines.append("process.analyze_2lss_1tau.process = cms.string('%s')" % sample_category)
    lepton_frWeight = None
    if applyFakeRateWeights == "disabled":
      lepton_frWeight = "disabled"
    else:
      lepton_frWeight = "enabled"
    histogramDir = getHistogramDir(lepton_selection, lepton_frWeight, lepton_charge_selection)
    lines.append("process.analyze_2lss_1tau.histogramDir = cms.string('%s')" % histogramDir)
    lines.append("process.analyze_2lss_1tau.era = cms.string('%s')" % era)
    lines.append("process.analyze_2lss_1tau.triggers_1e = cms.vstring(%s)" % self.triggers_1e)
    lines.append("process.analyze_2lss_1tau.use_triggers_1e = cms.bool(%s)" % ("1e" in triggers))
    lines.append("process.analyze_2lss_1tau.triggers_2e = cms.vstring(%s)" % self.triggers_2e)
    lines.append("process.analyze_2lss_1tau.use_triggers_2e = cms.bool(%s)" % ("2e" in triggers))
    lines.append("process.analyze_2lss_1tau.triggers_1mu = cms.vstring(%s)" % self.triggers_1mu)
    lines.append("process.analyze_2lss_1tau.use_triggers_1mu = cms.bool(%s)" % ("1mu" in triggers))
    lines.append("process.analyze_2lss_1tau.triggers_2mu = cms.vstring(%s)" % self.triggers_2mu)
    lines.append("process.analyze_2lss_1tau.use_triggers_2mu = cms.bool(%s)" % ("2mu" in triggers))
    lines.append("process.analyze_2lss_1tau.triggers_1e1mu = cms.vstring(%s)" % self.triggers_1e1mu)
    lines.append("process.analyze_2lss_1tau.use_triggers_1e1mu = cms.bool(%s)" % ("1e1mu" in triggers))
    lines.append("process.analyze_2lss_1tau.leptonSelection = cms.string('%s')" % lepton_selection)
    lines.append("process.analyze_2lss_1tau.apply_leptonGenMatching = cms.bool(%s)" % (apply_leptonGenMatching and is_mc))
    lines.append("process.analyze_2lss_1tau.leptonChargeSelection = cms.string('%s')" % lepton_charge_selection)
    lines.append("process.analyze_2lss_1tau.hadTauSelection = cms.string('%s')" % hadTau_selection)
    lines.append("process.analyze_2lss_1tau.apply_hadTauGenMatching = cms.bool(%s)" % (apply_hadTauGenMatching and is_mc))
    lines.append("process.analyze_2lss_1tau.applyFakeRateWeights = cms.string('%s')" % applyFakeRateWeights)
    if hadTau_selection.find("Fakeable") != -1 and applyFakeRateWeights in [ "3L", "2tau" ]:
      fitFunctionName = None
      if era == "2015":
        lines.append("process.analyze_2lss_1tau.hadTauFakeRateWeight.inputFileName = cms.string('tthAnalysis/HiggsToTauTau/data/FR_tau_2015.root')")
        # CV: use data/MC corrections determined for dR03mvaLoose discriminator,
        #     as the event statistics in 2015 data is too low to determine data/MC corrections for tighter working-points
        fitFunctionName = "jetToTauFakeRate/dR03mvaLoose/$etaBin/fitFunction_data_div_mc_hadTaus_pt"        
      elif era == "2016":
        lines.append("process.analyze_2lss_1tau.hadTauFakeRateWeight.inputFileName = cms.string('tthAnalysis/HiggsToTauTau/data/FR_tau_2016.root')")
        # CV: use data/MC corrections determined for dR03mvaMedium discriminator for 2016 data
        fitFunctionName = "jetToTauFakeRate/dR03mvaMedium/$etaBin/fitFunction_data_div_mc_hadTaus_pt"   
      else:
        raise ValueError("Invalid parameter 'era' = %s !!" % era)
      lines.append("process.analyze_2lss_1tau.hadTauFakeRateWeight.lead.fitFunctionName = cms.string('%s')" % fitFunctionName)
    if hadTau_selection.find("mcClosure") != -1:
      lines.append("process.analyze_2lss_1tau.hadTauFakeRateWeight.applyFitFunction_lead = cms.bool(False)")
      lines.append("process.analyze_2lss_1tau.hadTauFakeRateWeight.applyFitFunction_sublead = cms.bool(False)")
    lines.append("process.analyze_2lss_1tau.isMC = cms.bool(%s)" % is_mc)
    lines.append("process.analyze_2lss_1tau.central_or_shift = cms.string('%s')" % central_or_shift)
    lines.append("process.analyze_2lss_1tau.lumiScale = cms.double(%f)" % lumi_scale)
    lines.append("process.analyze_2lss_1tau.apply_genWeight = cms.bool(%s)" % apply_genWeight)
    lines.append("process.analyze_2lss_1tau.apply_trigger_bits = cms.bool(%s)" % apply_trigger_bits)
    lines.append("process.analyze_2lss_1tau.selEventsFileName_output = cms.string('%s')" % rle_output_file)
    create_cfg(self.cfgFile_analyze_original, cfgFile_modified, lines)

  def createCfg_addBackgrounds(self, inputFile, outputFile, cfgFile_modified, categories, processes_input, process_output):
    """Create python configuration file for the addBackgrounds executable (sum either all "fake" or all "non-fake" contributions)

    Args:
      inputFiles: input file (the ROOT file produced by hadd_stage1)
      outputFile: output file of the job
    """  
    lines = []
    lines.append("process.fwliteInput.fileNames = cms.vstring('%s')" % inputFile)
    lines.append("process.fwliteOutput.fileName = cms.string('%s')" % outputFile)
    lines.append("process.addBackgrounds.categories = cms.vstring(%s)" % categories)
    lines.append("process.addBackgrounds.processes_input = cms.vstring(%s)" % processes_input)
    lines.append("process.addBackgrounds.process_output = cms.string('%s')" % process_output)
    create_cfg(self.cfgFile_addBackgrounds_original, cfgFile_modified, lines)

  def createCfg_addFakes(self, inputFile, outputFile, cfgFile_modified, category_signal, category_sideband):
    """Create python configuration file for the addBackgroundLeptonFakes executable (data-driven estimation of 'Fakes' backgrounds)

    Args:
      inputFiles: input file (the ROOT file produced by hadd_stage1)
      outputFile: output file of the job
    """  
    lines = []
    lines.append("process.fwliteInput.fileNames = cms.vstring('%s')" % inputFile)
    lines.append("process.fwliteOutput.fileName = cms.string('%s')" % outputFile)
    lines.append("process.addBackgroundLeptonFakes.categories = cms.VPSet(")
    lines.append("    cms.PSet(")
    lines.append("        signal = cms.string('%s')," % category_signal) 
    lines.append("        sideband = cms.string('%s')" % category_sideband)
    lines.append("    )")
    lines.append(")")
    processesToSubtract = self.nonfake_backgrounds
    ##processesToSubtract.append("fakes_signal")
    lines.append("process.addBackgroundLeptonFakes.processesToSubtract = cms.vstring(%s)" % processesToSubtract)
    create_cfg(self.cfgFile_addFakes_original, cfgFile_modified, lines)

  def createCfg_addFlips(self, inputFile, outputFile, cfgFile_modified):
    """Create python configuration file for the addBackgroundLeptonFlips executable (data-driven estimation of 'Flips' backgrounds)

    Args:
      inputFiles: input file (the ROOT file produced by hadd_stage1)
      outputFile: output file of the job
    """  
    lines = []
    lines.append("process.fwliteInput.fileNames = cms.vstring('%s')" % inputFile)
    lines.append("process.fwliteOutput.fileName = cms.string('%s')" % outputFile)
    lines.append("process.addBackgroundLeptonFlips.processesToSubtract = cms.vstring(%s)" % self.nonfake_backgrounds)
    create_cfg(self.cfgFile_addFlips_original, cfgFile_modified, lines)

  def createCfg_makePlots_mcClosure(self):
    """Fills the template of python configuration file for making control plots

    Args:
      histogramFile: name of the input ROOT file 
    """
    lines = []
    lines.append("process.fwliteInput.fileNames = cms.vstring('%s')" % self.histogramFile_hadd_stage2)
    lines.append("process.makePlots_mcClosure.outputFileName = cms.string('%s')" % os.path.join(self.outputDir, DKEY_PLOT, self.channel, "makePlots_mcClosure_%s.png" % self.channel))
    lines.append("process.makePlots_mcClosure.processesBackground = cms.vstring(%s)" % self.make_plots_backgrounds)
    lines.append("process.makePlots_mcClosure.processSignal = cms.string('%s')" % self.make_plots_signal)
    lines.append("process.makePlots_mcClosure.categories = cms.VPSet(")
    lines.append("  cms.PSet(")
    lines.append("    signal = cms.string('%s')," % self.histogramDir_prep_dcard)
    lines.append("    sideband = cms.string('%s')," % self.histogramDir_prep_dcard.replace("Tight", "Fakeable_mcClosure_wFakeRateWeights"))
    lines.append("    label = cms.string('%s')" % self.channel)
    lines.append("  )")
    lines.append(")")
    lines.append("process.makePlots_mcClosure.distributions = cms.VPSet(")
    lines.append("  cms.PSet(")
    lines.append("    histogramName = cms.string('sel/evt/$PROCESS/numJets'),")
    lines.append("    xAxisTitle = cms.string('jet Multiplicity'),")
    lines.append("    yAxisTitle = cms.string('N')")
    lines.append("  ),")
    lines.append("  cms.PSet(")
    lines.append("    histogramName = cms.string('sel/evt/$PROCESS/mvaDiscr_2lss'),")
    lines.append("    xAxisTitle = cms.string('MVA'),")
    lines.append("    yAxisTitle = cms.string('dN/dMVA')")
    lines.append("  ),")
    lines.append("  cms.PSet(")
    lines.append("    histogramName = cms.string('sel/evt/$PROCESS/mTauTauVis'),")
    lines.append("    xAxisTitle = cms.string('m_{#tau#tau}^{vis} [GeV]'),")
    lines.append("    yAxisTitle = cms.string('dN/dm_{#tau#tau}^{vis} [1/GeV]')")
    lines.append("  )")
    lines.append(")")
    cfgFile_modified = os.path.join(self.outputDir, DKEY_CFGS, "makePlots_mcClosure_%s_cfg.py" % self.channel)
    create_cfg(self.cfgFile_make_plots_original, cfgFile_modified, lines)
    self.cfgFiles_make_plots_mcClosure_modified.append(cfgFile_modified)

  def addToMakefile_addBackgrounds(self, lines_makefile):
    for key in self.histogramFile_addBackgrounds.keys():
      lines_makefile.append("%s: %s" % (self.histogramFile_addBackgrounds[key], self.histogramFile_hadd_stage1))
      lines_makefile.append("\t%s %s" % (self.executable_addBackgrounds, self.cfgFile_addBackgrounds_modified[key]))
      lines_makefile.append("")
      self.filesToClean.append(self.histogramFile_addBackgrounds[key])

  def addToMakefile_addFakes(self, lines_makefile):
    for key in self.histogramFile_addFakes.keys():
      lines_makefile.append("%s: %s" % (self.histogramFile_addFakes[key], self.histogramFile_hadd_stage1_5))
      lines_makefile.append("\t%s %s" % (self.executable_addFakes, self.cfgFile_addFakes_modified[key]))
      lines_makefile.append("")
      self.filesToClean.append(self.histogramFile_addFakes[key])

  def addToMakefile_addFlips(self, lines_makefile):
    lines_makefile.append("%s: %s" % (self.histogramFile_addFlips, self.histogramFile_hadd_stage1_5))
    lines_makefile.append("\t%s %s" % (self.executable_addFlips, self.cfgFile_addFlips_modified))
    lines_makefile.append("")
    self.filesToClean.append(self.histogramFile_addFlips)

  def addToMakefile_backgrounds_from_data(self, lines_makefile):
    self.addToMakefile_addBackgrounds(lines_makefile)
    self.inputFiles_hadd_stage1_5 = [ self.histogramFile_hadd_stage1 ]
    for key in self.histogramFile_addBackgrounds.keys():
      self.inputFiles_hadd_stage1_5.append(self.histogramFile_addBackgrounds[key])
    self.addToMakefile_hadd_stage1_5(lines_makefile)
    self.addToMakefile_addFakes(lines_makefile)
    self.addToMakefile_addFlips(lines_makefile)

  def addToMakefile_make_plots_mcClosure(self, lines_makefile):
    """Adds the commands to Makefile that are necessary for making control plots of the jet->tau fake background estimation procedure.
    """
    for idxJob, cfgFile_modified in enumerate(self.cfgFiles_make_plots_mcClosure_modified):
      lines_makefile.append("makePlots_mcClosure%i: %s" % (idxJob, self.histogramFile_hadd_stage2))
      lines_makefile.append("\t%s %s" % (self.executable_make_plots, cfgFile_modified))
      lines_makefile.append("")

  def create(self):
    """Creates all necessary config files and runs the complete analysis workfow -- either locally or on the batch system
    """

    for key in self.dirs.keys():
      if type(self.dirs[key]) == dict:
        for dir_type in self.dirs[key].keys():
          create_if_not_exists(self.dirs[key][dir_type])
      else:
        create_if_not_exists(self.dirs[key])
  
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"] or sample_info["sample_category"] in [ "additional_signal_overlap", "background_data_estimate" ]:
        continue

      process_name = sample_info["process_name_specific"]

      logging.info("Creating configuration files to run '%s' for sample %s" % (self.executable_analyze, process_name))  
    
      is_mc = (sample_info["type"] == "mc")
      lumi_scale = 1. if not (self.use_lumi and is_mc) else sample_info["xsection"] * self.lumi / sample_info["nof_events"]
      apply_genWeight = sample_info["apply_genWeight"] if (is_mc and "apply_genWeight" in sample_info.keys()) else False
      sample_category = sample_info["sample_category"]
      triggers = sample_info["triggers"]
      apply_trigger_bits = (is_mc and (self.era == "2015" or (self.era == "2016" and sample_info["reHLT"]))) or not is_mc

      for lepton_and_hadTau_selection in self.lepton_and_hadTau_selections:
        lepton_selection = lepton_and_hadTau_selection
        hadTau_selection = lepton_and_hadTau_selection
        if self.applyFakeRateWeights == "2lepton":
          hadTau_selection = "Tight"
        hadTau_selection = "|".join([ hadTau_selection, self.hadTau_selection_part2 ])        
        for lepton_and_hadTau_frWeight in self.lepton_and_hadTau_frWeights:
          if lepton_and_hadTau_frWeight == "enabled" and not lepton_and_hadTau_selection.startswith("Fakeable"):
            continue
          if lepton_and_hadTau_selection == "Fakeable_mcClosure" and not lepton_and_hadTau_frWeight == "enabled":
            continue
          lepton_and_hadTau_selection_and_frWeight = get_lepton_and_hadTau_selection_and_frWeight(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight)
          
          for lepton_charge_selection in self.lepton_charge_selections:
            for central_or_shift in self.central_or_shifts:

              inputFileList = generateInputFileList(sample_name, sample_info, self.max_files_per_job, self.debug)
              for jobId in inputFileList.keys():
                if central_or_shift != "central" and not (lepton_and_hadTau_selection.startswith("Tight") and lepton_charge_selection == "SS"):
                  continue
                if central_or_shift != "central" and not is_mc:
                  continue                
                if central_or_shift.startswith("CMS_ttHl_thu_shape_ttH") and sample_category != "signal":
                  continue
                if central_or_shift.startswith("CMS_ttHl_thu_shape_ttW") and sample_category != "TTW":
                  continue
                if central_or_shift.startswith("CMS_ttHl_thu_shape_ttZ") and sample_category != "TTZ":
                  continue
  
                key_dir = getKey(sample_name, lepton_and_hadTau_selection, lepton_and_hadTau_frWeight, lepton_charge_selection)
                key_file = getKey(sample_name, lepton_and_hadTau_selection, lepton_and_hadTau_frWeight, lepton_charge_selection, central_or_shift, jobId)

                self.ntupleFiles[key_file] = inputFileList[jobId]
                if len(self.ntupleFiles[key_file]) == 0:
                  print "Warning: ntupleFiles['%s'] = %s --> skipping job !!" % (key_file, self.ntupleFiles[key_file])
                  continue
                self.cfgFiles_analyze_modified[key_file] = os.path.join(self.dirs[key_dir][DKEY_CFGS], "analyze_%s_%s_%s_%s_%s_%i_cfg.py" % \
                  (self.channel, process_name, lepton_and_hadTau_selection_and_frWeight, lepton_charge_selection, central_or_shift, jobId))
                self.histogramFiles[key_file] = os.path.join(self.dirs[key_dir][DKEY_HIST], "%s_%s_%s_%s_%i.root" % \
                  (process_name, lepton_and_hadTau_selection_and_frWeight, lepton_charge_selection, central_or_shift, jobId))
                self.logFiles_analyze[key_file] = os.path.join(self.dirs[key_dir][DKEY_LOGS], "analyze_%s_%s_%s_%s_%s_%i.log" % \
                  (self.channel, process_name, lepton_and_hadTau_selection_and_frWeight, lepton_charge_selection, central_or_shift, jobId))
                self.rleOutputFiles[key_file] = os.path.join(self.dirs[key_dir][DKEY_RLES], "rle_%s_%s_%s_%s_%s_%i.txt" % \
                  (self.channel, process_name, lepton_and_hadTau_selection_and_frWeight, lepton_charge_selection, central_or_shift, jobId)) if self.select_rle_output else ""
                
                applyFakeRateWeights = self.applyFakeRateWeights
                if lepton_and_hadTau_frWeight == "disabled":
                  applyFakeRateWeights = "disabled"
                self.createCfg_analyze(self.ntupleFiles[key_file], self.histogramFiles[key_file], sample_category, self.era, triggers,
                  lepton_selection, self.apply_leptonGenMatching, lepton_charge_selection, hadTau_selection, self.apply_hadTauGenMatching,
                  applyFakeRateWeights, is_mc, central_or_shift, lumi_scale, apply_genWeight, apply_trigger_bits, self.cfgFiles_analyze_modified[key_file],
                  self.rleOutputFiles[key_file])
                
    if self.is_sbatch:
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
      self.createScript_sbatch()

    for key in self.histogramFiles.keys():
      self.inputFiles_hadd_stage1.append(self.histogramFiles[key])

    logging.info("Creating configuration files for executing 'addBackgrounds'")  
    process_names = []
    process_names.extend(self.nonfake_backgrounds)
    process_names.extend([ "signal", "ttH_htt", "ttH_hww", "ttH_hzz" ])
    # sum non-fake contributions for each MC sample separately
    # input processes: TT2l0j,...
    # output processes: TT; ...
    for process_name in process_names:
      for lepton_and_hadTau_selection in self.lepton_and_hadTau_selections:
        for lepton_and_hadTau_frWeight in self.lepton_and_hadTau_frWeights:
          if lepton_and_hadTau_frWeight == "enabled" and not lepton_and_hadTau_selection.startswith("Fakeable"):
            continue
          if lepton_and_hadTau_selection == "Fakeable_mcClosure" and not lepton_and_hadTau_frWeight == "enabled":
            continue
          lepton_and_hadTau_selection_and_frWeight = get_lepton_and_hadTau_selection_and_frWeight(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight)
          for lepton_charge_selection in self.lepton_charge_selections:
            key = getKey(process_name, lepton_and_hadTau_selection, lepton_and_hadTau_frWeight, lepton_charge_selection)
            self.histogramFile_addBackgrounds[key] = os.path.join(self.outputDir, DKEY_HIST, "addBackgrounds_%s_%s_%s_%s.root" % \
              (self.channel, process_name, lepton_and_hadTau_selection_and_frWeight, lepton_charge_selection))        
            self.cfgFile_addBackgrounds_modified[key] = os.path.join(self.outputDir, DKEY_CFGS, "addBackgrounds_%s_%s_%s_%s_cfg.py" % \
              (self.channel, process_name, lepton_and_hadTau_selection_and_frWeight, lepton_charge_selection))
            histogramDir = getHistogramDir(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight, lepton_charge_selection)
            processes_input = [ "%s%s" % (process_name, genMatch) for genMatch in self.lepton_and_hadTau_genMatches_nonfakes ]
            # CV: treat fakes in ttH signal events as "signal", not as "background"
            ##if process_name in [ "signal", "ttH_htt", "ttH_hww", "ttH_hzz" ]:
            ##  processes_input.extend([ "%s%s" % (process_name, genMatch) for genMatch in self.lepton_and_hadTau_genMatches_fakes ])
            self.process_output_addBackgrounds[key] = process_name
            self.createCfg_addBackgrounds(self.histogramFile_hadd_stage1, self.histogramFile_addBackgrounds[key], self.cfgFile_addBackgrounds_modified[key],
              [ histogramDir ], processes_input, self.process_output_addBackgrounds[key])
    # sum fake contributions for each MC sample separately
    # input processes: TT1l1j,TT0l2j,...
    # output processes: fakes_TT; ...
    for process_name in process_names:
      for lepton_and_hadTau_selection in self.lepton_and_hadTau_selections:
        for lepton_and_hadTau_frWeight in self.lepton_and_hadTau_frWeights:
          if lepton_and_hadTau_frWeight == "enabled" and not lepton_and_hadTau_selection.startswith("Fakeable"):
            continue
          if lepton_and_hadTau_selection == "Fakeable_mcClosure" and not lepton_and_hadTau_frWeight == "enabled":
            continue
          lepton_and_hadTau_selection_and_frWeight = get_lepton_and_hadTau_selection_and_frWeight(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight)
          for lepton_charge_selection in self.lepton_charge_selections:
            key = getKey("fakes_%s" % process_name, lepton_and_hadTau_selection, lepton_and_hadTau_frWeight, lepton_charge_selection)
            self.histogramFile_addBackgrounds[key] = os.path.join(self.outputDir, DKEY_HIST, "addBackgrounds_%s_fakes_%s_%s_%s.root" % \
              (self.channel, process_name, lepton_and_hadTau_selection_and_frWeight, lepton_charge_selection))        
            self.cfgFile_addBackgrounds_modified[key] = os.path.join(self.outputDir, DKEY_CFGS, "addBackgrounds_%s_fakes_%s_%s_%s_cfg.py" % \
              (self.channel, process_name, lepton_and_hadTau_selection_and_frWeight, lepton_charge_selection))
            histogramDir = getHistogramDir(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight, lepton_charge_selection)
            processes_input = [ "%s%s" % (process_name, genMatch) for genMatch in self.lepton_and_hadTau_genMatches_fakes ]
            self.process_output_addBackgrounds[key] = "fakes_%s" % process_name
            self.createCfg_addBackgrounds(self.histogramFile_hadd_stage1, self.histogramFile_addBackgrounds[key], self.cfgFile_addBackgrounds_modified[key],
              [ histogramDir ], processes_input, self.process_output_addBackgrounds[key])
    # sum fake contributions for the total of all MC samples
    # input processes: TT1l1j,TT0l2j,...
    # output process: fakes_mc
    for lepton_and_hadTau_selection in self.lepton_and_hadTau_selections:
      for lepton_and_hadTau_frWeight in self.lepton_and_hadTau_frWeights:
        if lepton_and_hadTau_frWeight == "enabled" and not lepton_and_hadTau_selection.startswith("Fakeable"):
          continue
        if lepton_and_hadTau_selection == "Fakeable_mcClosure" and not lepton_and_hadTau_frWeight == "enabled":
          continue
        lepton_and_hadTau_selection_and_frWeight = get_lepton_and_hadTau_selection_and_frWeight(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight)
        for lepton_charge_selection in self.lepton_charge_selections:
          key = getKey(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight, lepton_charge_selection)
          self.histogramFile_addBackgrounds[key] = os.path.join(self.outputDir, DKEY_HIST, "addBackgrounds_%s_fakes_mc_%s_%s.root" % \
            (self.channel, lepton_and_hadTau_selection_and_frWeight, lepton_charge_selection))
          self.cfgFile_addBackgrounds_modified[key] = os.path.join(self.outputDir, DKEY_CFGS, "addBackgrounds_%s_fakes_mc_%s_%s_cfg.py" % \
            (self.channel, lepton_and_hadTau_selection_and_frWeight, lepton_charge_selection))
          histogramDir = getHistogramDir(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight, lepton_charge_selection)
          processes_input = []
          for process_name in self.nonfake_backgrounds:
            for genMatch in self.lepton_and_hadTau_genMatches_fakes:
              processes_input.append("%s%s" % (process_name, genMatch))
          self.process_output_addBackgrounds[key] = "fakes_mc"
          self.createCfg_addBackgrounds(self.histogramFile_hadd_stage1, self.histogramFile_addBackgrounds[key], self.cfgFile_addBackgrounds_modified[key],
            [ histogramDir ], processes_input, self.process_output_addBackgrounds[key])
        
    logging.info("Creating configuration files for executing 'addBackgroundLeptonFakes'")
    for lepton_charge_selection in self.lepton_charge_selections:
      key = getKey("fakes_data", lepton_charge_selection) 
      self.histogramFile_addFakes[key] = os.path.join(self.outputDir, DKEY_HIST, "addBackgroundLeptonFakes_%s_%s.root" % \
        (self.channel, lepton_charge_selection))
      self.cfgFile_addFakes_modified[key] = os.path.join(self.outputDir, DKEY_CFGS, "addBackgroundLeptonFakes_%s_%s_cfg.py" % \
        (self.channel, lepton_charge_selection))
      category_signal = "2lss_1tau_%s_Tight" % lepton_charge_selection
      category_sideband = "2lss_1tau_%s_Fakeable_wFakeRateWeights" % lepton_charge_selection
      self.createCfg_addFakes(self.histogramFile_hadd_stage1_5, self.histogramFile_addFakes[key], self.cfgFile_addFakes_modified[key],
        category_signal, category_sideband)

    logging.info("Creating configuration files for executing 'addBackgroundLeptonFlips'")
    self.createCfg_addFlips(self.histogramFile_hadd_stage1_5, self.histogramFile_addFlips, self.cfgFile_addFlips_modified)

    logging.info("Creating configuration files for executing 'prepareDatacards'")
    for histogramToFit in self.histograms_to_fit:
      self.createCfg_prep_dcard(histogramToFit)

    logging.info("Creating configuration files for executing 'makePlots'")
    self.createCfg_makePlots()
    if "OS" in self.lepton_charge_selections:
      make_plots_backgrounds = self.make_plots_backgrounds
      if "flips_data" in make_plots_backgrounds:
        make_plots_backgrounds.remove("flips_data")
      self.createCfg_makePlots(self.histogramDir_prep_dcard_OS, "OS", make_plots_backgrounds)
    if "Fakeable_mcClosure" in self.lepton_and_hadTau_selections:
      self.createCfg_makePlots_mcClosure()

    self.inputFiles_hadd_stage2 = [ self.histogramFile_hadd_stage1_5 ] + self.histogramFile_addFakes.values() + [ self.histogramFile_addFlips ]
    
    logging.info("Creating Makefile")
    lines_makefile = []
    self.addToMakefile_analyze(lines_makefile)
    self.addToMakefile_hadd_stage1(lines_makefile)
    self.addToMakefile_backgrounds_from_data(lines_makefile)
    self.addToMakefile_hadd_stage2(lines_makefile)
    self.addToMakefile_prep_dcard(lines_makefile)
    self.addToMakefile_make_plots(lines_makefile)
    self.addToMakefile_make_plots_mcClosure(lines_makefile)
    self.createMakefile(lines_makefile)
  
    logging.info("Done")

