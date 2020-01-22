#ifndef tthAnalysis_HiggsToTauTau_Data_to_MC_CorrectionInterface_2018_h
#define tthAnalysis_HiggsToTauTau_Data_to_MC_CorrectionInterface_2018_h

#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_Base.h"

class Data_to_MC_CorrectionInterface_2018
  : virtual public Data_to_MC_CorrectionInterface_Base
{
public:
  Data_to_MC_CorrectionInterface_2018(const edm::ParameterSet & cfg);
  ~Data_to_MC_CorrectionInterface_2018() override;

  //-----------------------------------------------------------------------------
  // data/MC correction for electron and muon trigger efficiency
  double
  getSF_leptonTriggerEff(TriggerSFsys central_or_shift) const override;
  //-----------------------------------------------------------------------------
};

#endif // tthAnalysis_HiggsToTauTau_data_to_MC_corrections_2018_h
