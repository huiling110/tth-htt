#include "tthAnalysis/HiggsToTauTau/interface/EvtHistManager_2lss_1tau.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // get_era(), kEra_*
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()

EvtHistManager_2lss_1tau::EvtHistManager_2lss_1tau(const edm::ParameterSet& cfg)
  : HistManagerBase(cfg)
  , era_(get_era(cfg.getParameter<std::string>("era")))
  , option_(kOption_undefined)
{
  const std::string option_string = cfg.getParameter<std::string>("option");
  if(option_string == "allHistograms")
  {
    option_ = kOption_allHistograms;
  }
  else if(option_string == "minimalHistograms")
  {
    option_ = kOption_minimalHistograms;
  }
  else
  {
    throw cmsException(__func__) << "Invalid Configuration parameter 'option' = " << option_string;
  }
  const std::vector<std::string> sysOpts_central = {
    "numElectrons",
    "numMuons",
    "numHadTaus",
    "numJets",
    "numBJets_loose",
    "numBJets_medium",
    "numBJets_loose_vs_numJets",
    "numBJets_medium_vs_numJets",
    "mvaOutput_2lss_ttV",
    "mvaOutput_2lss_tt",
    "mvaOutput_2lss_1tau_plainKin_tt",
    "mvaOutput_2lss_1tau_plainKin_ttV",
    "mvaOutput_2lss_1tau_plainKin_1B_M",
    "mvaOutput_2lss_1tau_plainKin_SUM_M",
    "mvaOutput_2lss_1tau_plainKin_SUM_M_noRebin",
    "mvaOutput_2lss_1tau_HTT_SUM_M",
    "mvaOutput_2lss_1tau_HTT_SUM_M_noRebin",
    "mvaOutput_2lss_1tau_HTTMEM_SUM_M",
    "mvaOutput_2lss_1tau_HTTMEM_SUM_M_noRebin",
    "mTauTauVis",
    "mTauTauVis1",
    "mTauTauVis2",
    "memOutput_LR",
  };
  const std::vector<std::string> sysOpts_all = {
    "mvaOutput_final",
    "EventCounter",
  };
  for(const std::string & sysOpt: sysOpts_central)
  {
    central_or_shiftOptions_[sysOpt] = { "central" };
  }
  for(const std::string & sysOpt: sysOpts_all)
  {
    central_or_shiftOptions_[sysOpt] = { "*" };
  }
}

const TH1 *
EvtHistManager_2lss_1tau::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_2lss_1tau::bookCategories(TFileDirectory & dir,
                                  const std::vector<std::string> & categories_sig_1p2_rest_1_th_1p2,
                                  const std::vector<std::string> & categories_sig_2_rest_2p2_th_2,
                                  const std::vector<std::string> & categories_sig_2_rest_2_th_2,
                                  const std::vector<std::string> & categories_sig_2_rest_2p5_th_2
                                )
{
  for(const std::string & category: categories_sig_1p2_rest_1_th_1p2)
  {
    histograms_by_category_sig_1p2_rest_1_th_1p2_[category] = book1D(dir, category, category, 40,  0., +1.);
    central_or_shiftOptions_[category] = { "*" };
  }
  for(const std::string & category: categories_sig_2_rest_2p2_th_2)
  {
    histograms_by_category_sig_2_rest_2p2_th_2_[category] = book1D(dir, category, category, 40,  0., +1.);
    central_or_shiftOptions_[category] = { "*" };
  }
  for(const std::string & category: categories_sig_2_rest_2_th_2)
  {
    histograms_by_category_sig_2_rest_2_th_2_[category] = book1D(dir, category, category, 40,  0., +1.);
    central_or_shiftOptions_[category] = { "*" };
  }
  for(const std::string & category: categories_sig_2_rest_2p5_th_2)
  {
    histograms_by_category_sig_2_rest_2p5_th_2_[category] = book1D(dir, category, category, 40,  0., +1.);
    central_or_shiftOptions_[category] = { "*" };
  }
}

void EvtHistManager_2lss_1tau::bookHistograms(TFileDirectory & dir)
{
  if(option_ == kOption_allHistograms)
  {
    histogram_numElectrons_    = book1D(dir, "numElectrons",    "numElectrons",     5, -0.5,  +4.5);
    histogram_numMuons_        = book1D(dir, "numMuons",        "numMuons",         5, -0.5,  +4.5);
    histogram_numHadTaus_      = book1D(dir, "numHadTaus",      "numHadTaus",       5, -0.5,  +4.5);
    histogram_numJets_         = book1D(dir, "numJets",         "numJets",         20, -0.5, +19.5);
    histogram_numBJets_loose_  = book1D(dir, "numBJets_loose",  "numBJets_loose",  10, -0.5,  +9.5);
    histogram_numBJets_medium_ = book1D(dir, "numBJets_medium", "numBJets_medium", 10, -0.5,  +9.5);

    histogram_mvaOutput_2lss_ttV_ = book1D(dir, "mvaOutput_2lss_ttV", "mvaOutput_2lss_ttV", 40, -1., +1.);
    histogram_mvaOutput_2lss_tt_  = book1D(dir, "mvaOutput_2lss_tt",  "mvaOutput_2lss_tt",  40, -1., +1.);

    histogram_mvaOutput_2lss_1tau_plainKin_tt_            = book1D(dir, "mvaOutput_2lss_1tau_plainKin_tt",            "mvaOutput_2lss_1tau_plainKin_tt",            40, -1., +1.);
    histogram_mvaOutput_2lss_1tau_plainKin_ttV_           = book1D(dir, "mvaOutput_2lss_1tau_plainKin_ttV",           "mvaOutput_2lss_1tau_plainKin_ttV",           40, -1., +1.);
    histogram_mvaOutput_2lss_1tau_plainKin_1B_M_          = book1D(dir, "mvaOutput_2lss_1tau_plainKin_1B_M",          "mvaOutput_2lss_1tau_plainKin_1B_M",          40, -1., +1.);
    histogram_mvaOutput_2lss_1tau_plainKin_SUM_M_         = book1D(dir, "mvaOutput_2lss_1tau_plainKin_SUM_M",         "mvaOutput_2lss_1tau_plainKin_SUM_M",         40, -1., +1.);
    histogram_mvaOutput_2lss_1tau_plainKin_SUM_M_noRebin_ = book1D(dir, "mvaOutput_2lss_1tau_plainKin_SUM_M_noRebin", "mvaOutput_2lss_1tau_plainKin_SUM_M_noRebin", 40, -1., +1.);
    histogram_mvaOutput_2lss_1tau_HTT_SUM_M_              = book1D(dir, "mvaOutput_2lss_1tau_HTT_SUM_M",              "mvaOutput_2lss_1tau_HTT_SUM_M",              40, -1., +1.);
    histogram_mvaOutput_2lss_1tau_HTT_SUM_M_noRebin_      = book1D(dir, "mvaOutput_2lss_1tau_HTT_SUM_M_noRebin",      "mvaOutput_2lss_1tau_HTT_SUM_M_noRebin",      40, -1., +1.);
    histogram_mvaOutput_2lss_1tau_HTTMEM_SUM_M_           = book1D(dir, "mvaOutput_2lss_1tau_HTTMEM_SUM_M",           "mvaOutput_2lss_1tau_HTTMEM_SUM_M",           40, -1., +1.);
    histogram_mvaOutput_2lss_1tau_HTTMEM_SUM_M_noRebin_   = book1D(dir, "mvaOutput_2lss_1tau_HTTMEM_SUM_M_noRebin",   "mvaOutput_2lss_1tau_HTTMEM_SUM_M_noRebin",   40, -1., +1.);
  }

  Float_t binsx[12]  = { 0.0, 0.14, 0.18, 0.22, 0.28, 0.32, 0.35, 0.38, 0.43, 0.47, 0.53, 1.0 };
  histogram_final_  = book1D(dir, "mvaOutput_final",  "mvaOutput_final", 11, binsx);

  histogram_mTauTauVis_   = book1D(dir, "mTauTauVis",   "mTauTauVis",    20,  0., 200.);
  histogram_mTauTauVis1_  = book1D(dir, "mTauTauVis1",  "mTauTauVis1",   20,  0., 200.);
  histogram_mTauTauVis2_  = book1D(dir, "mTauTauVis2",  "mTauTauVis2",   20,  0., 200.);
  histogram_memOutput_LR_ = book1D(dir, "memOutput_LR", "memOutput_LR", 100,  0.,   1.);

  histogram_EventCounter_ = book1D(dir, "EventCounter", "EventCounter",   1, -0.5, +0.5);
}

void
EvtHistManager_2lss_1tau::fillHistograms(int numElectrons,
                                         int numMuons,
                                         int numHadTaus,
                                         int numJets,
                                         int numBJets_loose,
                                         int numBJets_medium,
                                         double evtWeight,
                                         double mvaOutput_2lss_ttV,
                                         double mvaOutput_2lss_tt,
                                         double mvaOutput_2lss_1tau_plainKin_tt,
                                         double mvaOutput_2lss_1tau_plainKin_ttV,
                                         double mvaOutput_2lss_1tau_plainKin_1B_M,
                                         double mvaOutput_2lss_1tau_plainKin_SUM_M,
                                         double mvaOutput_2lss_1tau_HTT_SUM_M,
                                         double mvaOutput_2lss_1tau_HTTMEM_SUM_M,
                                         double mTauTauVis1,
                                         double mTauTauVis2,
                                         double memOutput_LR,
                                         const std::string & category_3l_sig_1p2_rest_1_th_1p2_TF,
                                         double output_NN_sig_1p2_rest_1_th_1p2,
                                         const std::string & category_sig_2_rest_2p2_th_2_TF,
                                         double output_sig_2_rest_2p2_th_2,
                                         const std::string & category_sig_2_rest_2_th_2_TF,
                                         double output_NN_sig_2_rest_2_th_2,
                                         const std::string & category_sig_2_rest_2p5_th_2_TF,
                                         double output_NN_sig_2_rest_2p5_th_2
                                       )
{
  const double evtWeightErr = 0.;

  if(option_ == kOption_allHistograms)
  {
    fillWithOverFlow(histogram_numElectrons_,    numElectrons,    evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_numMuons_,        numMuons,        evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_numHadTaus_,      numHadTaus,      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_numJets_,         numJets,         evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_numBJets_loose_,  numBJets_loose,  evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_numBJets_medium_, numBJets_medium, evtWeight, evtWeightErr);

    fillWithOverFlow(histogram_mvaOutput_2lss_ttV_, mvaOutput_2lss_ttV, evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_mvaOutput_2lss_tt_,  mvaOutput_2lss_tt,  evtWeight, evtWeightErr);

    fillWithOverFlow(histogram_mvaOutput_2lss_1tau_plainKin_tt_,            mvaOutput_2lss_1tau_plainKin_tt,    evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_mvaOutput_2lss_1tau_plainKin_ttV_,           mvaOutput_2lss_1tau_plainKin_ttV,   evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_mvaOutput_2lss_1tau_plainKin_1B_M_,          mvaOutput_2lss_1tau_plainKin_1B_M,  evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_mvaOutput_2lss_1tau_plainKin_SUM_M_,         mvaOutput_2lss_1tau_plainKin_SUM_M, evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_mvaOutput_2lss_1tau_plainKin_SUM_M_noRebin_, mvaOutput_2lss_1tau_plainKin_SUM_M, evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_mvaOutput_2lss_1tau_HTTMEM_SUM_M_noRebin_,   mvaOutput_2lss_1tau_HTTMEM_SUM_M,   evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_mvaOutput_2lss_1tau_HTTMEM_SUM_M_,           mvaOutput_2lss_1tau_HTTMEM_SUM_M,   evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_mvaOutput_2lss_1tau_HTT_SUM_M_noRebin_,      mvaOutput_2lss_1tau_HTT_SUM_M,      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_mvaOutput_2lss_1tau_HTT_SUM_M_,              mvaOutput_2lss_1tau_HTT_SUM_M,      evtWeight, evtWeightErr);
  }
  fillWithOverFlow(histogram_final_,                                      mvaOutput_2lss_1tau_HTT_SUM_M,      evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mTauTauVis_,   mTauTauVis1,  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mTauTauVis1_,  mTauTauVis1,  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mTauTauVis2_,  mTauTauVis2,  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_memOutput_LR_, memOutput_LR, evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_EventCounter_, 0., evtWeight, evtWeightErr);

  if(! histograms_by_category_sig_1p2_rest_1_th_1p2_.count(category_3l_sig_1p2_rest_1_th_1p2_TF))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_3l_sig_1p2_rest_1_th_1p2_TF << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_sig_1p2_rest_1_th_1p2_[category_3l_sig_1p2_rest_1_th_1p2_TF], output_NN_sig_1p2_rest_1_th_1p2, evtWeight, evtWeightErr);
  //////////////////////////////////////////////////
  if(! histograms_by_category_sig_2_rest_2p2_th_2_.count(category_sig_2_rest_2p2_th_2_TF))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_sig_2_rest_2p2_th_2_TF << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_sig_2_rest_2p2_th_2_[category_sig_2_rest_2p2_th_2_TF], output_sig_2_rest_2p2_th_2, evtWeight, evtWeightErr);
  //////////////////////////////////////////////////
  if(! histograms_by_category_sig_2_rest_2_th_2_.count(category_sig_2_rest_2_th_2_TF))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_sig_2_rest_2_th_2_TF << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_sig_2_rest_2_th_2_[category_sig_2_rest_2_th_2_TF], output_NN_sig_2_rest_2_th_2, evtWeight, evtWeightErr);
  ////////////////////////////////////////////////
  if(! histograms_by_category_sig_2_rest_2p5_th_2_.count(category_sig_2_rest_2p5_th_2_TF))
  {
    throw cmsException(this, __func__, __LINE__) << "Histogram of the name '" << category_sig_2_rest_2p5_th_2_TF << "' was never booked";
  }
  fillWithOverFlow(histograms_by_category_sig_2_rest_2p5_th_2_[category_sig_2_rest_2p5_th_2_TF], output_NN_sig_2_rest_2p5_th_2, evtWeight, evtWeightErr);

}
