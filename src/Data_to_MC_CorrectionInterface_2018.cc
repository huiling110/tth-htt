#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2018.h"

#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h" // lutWrapperTH2
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // as_integer()

#include "TauPOG/TauIDSFs/interface/TauIDSFTool.h" // TauIDSFTool

#include <cmath> // std::fabs(), std::sqrt()

Data_to_MC_CorrectionInterface_2018::Data_to_MC_CorrectionInterface_2018(const edm::ParameterSet & cfg)
  : Data_to_MC_CorrectionInterface_Base(cfg)
{
#if 0
  throw cmsException(this, __func__, __LINE__)
    << "Not available in 2018 era"
  ;
#endif
#pragma message "Setting data-to-MC corrections to 1 in 2018"

  // Reconstruction efficiencies of electrons, measured by EGamma POG
  // https://twiki.cern.ch/twiki/pub/CMS/EgammaIDRecipesRun2/egammaEffi.txt_EGM2D_updatedAll.root
  sfElectronID_and_Iso_loose_.push_back(new lutWrapperTH2(
    inputFiles_,
    "tthAnalysis/HiggsToTauTau/data/leptonSF/2018/el_scaleFactors_gsf.root",
    "EGamma_SF2D",
    lut::kXetaYpt, -2.5, +2.5, lut::kLimit, 10., -1., lut::kLimit_and_Cut
  ));

  if(applyHadTauSF_)
  {
    const std::string tauIDSFTool_era = "2018ReReco";
    tauIdSFs_ = new TauIDSFTool(tauIDSFTool_era, tauIDSF_str_, tauIDSF_level_str_, false);
    initAntiEle_tauIDSFs(tauIDSFTool_era);
    initAntiMu_tauIDSFs(tauIDSFTool_era);
  }
}

Data_to_MC_CorrectionInterface_2018::~Data_to_MC_CorrectionInterface_2018()
{}

double
Data_to_MC_CorrectionInterface_2018::getWeight_leptonTriggerEff() const
{
#if 0
  throw cmsException(this, __func__, __LINE__)
    << "Not available in 2018 era"
  ;
#endif
#pragma message "Setting data-to-MC corrections to 1 in 2018"
  return 1.;
}

double
Data_to_MC_CorrectionInterface_2018::getSF_leptonTriggerEff(TriggerSFsys central_or_shift) const
{
#if 0
  throw cmsException(this, __func__, __LINE__)
    << "Not available in 2018 era"
  ;
#endif
#pragma message "Setting data-to-MC corrections to 1 in 2018"
  return 1.;
}
