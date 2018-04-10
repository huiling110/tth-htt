#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorTight.h" // RecoElectronSelectorTight

#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // kEra_2017
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException(), assert()

RecoElectronSelectorTight::RecoElectronSelectorTight(int era,
                                                     int index,
                                                     bool debug,
                                                     bool set_selection_flags)
  : era_(era)
  , set_selection_flags_(set_selection_flags)
  , apply_offline_e_trigger_cuts_(true)
  , debug_(debug)
  , min_pt_(7.)
  , max_absEta_(2.5)
  , max_dxy_(0.05)
  , max_dz_(0.1)
  , max_relIso_(0.4)
  , max_sip3d_(8.)
  , mvaPOGwp_(EGammaPOG::kWPL)
  , binning_absEta_({ 0.8, 1.479 })
  , min_pt_trig_(-1.) // Lines:237-240 in AN_2017_029_V5
  , max_sigmaEtaEta_trig_({ 0.011, 0.011, 0.030 })
  , max_HoE_trig_({ 0.10, 0.10, 0.07 })
  , max_deltaEta_trig_({ 0.01, 0.01, 0.008 })
  , max_deltaPhi_trig_({ 0.04, 0.04, 0.07 })
  , min_OoEminusOoP_trig_(-0.05)
  , max_OoEminusOoP_trig_({ 0.010, 0.010, 0.005 })
  , apply_conversionVeto_(true)
  , max_nLostHits_(0)
  , min_mvaTTH_(0.90) // Table 7 in AN2017_029_v5
{
  switch(era_)
  {
    case kEra_2017:
    {
      max_jetBtagCSV_ = BtagWP_CSV_2016.at(BtagWP::kMedium); // Table 7 in AN2017_029_v5
      break;
    }
    default: throw cmsException(this) << "Invalid era: " << era_;
  }
  assert(binning_absEta_.size() == 2);
  assert(max_sigmaEtaEta_trig_.size() == 3);
  assert(max_HoE_trig_.size() == 3);
  assert(max_deltaEta_trig_.size() == 3);
  assert(max_deltaPhi_trig_.size() == 3);
  assert(max_OoEminusOoP_trig_.size() == 3);
}

void
RecoElectronSelectorTight::enable_offline_e_trigger_cuts()
{
  apply_offline_e_trigger_cuts_ = true;
}

void
RecoElectronSelectorTight::disable_offline_e_trigger_cuts()
{
  apply_offline_e_trigger_cuts_ = false;
}

// enable/disable photon conversion veto
void
RecoElectronSelectorTight::enable_conversionVeto()
{
  apply_conversionVeto_ = true;
}

void
RecoElectronSelectorTight::disable_conversionVeto()
{
  apply_conversionVeto_ = false;
}

void
RecoElectronSelectorTight::set_selection_flags(bool selection_flag)
{
  set_selection_flags_ = selection_flag;
}

bool
RecoElectronSelectorTight::operator()(const RecoElectron & electron) const
{
  if(debug_)
  {
    std::cout << get_human_line(this, __func__) << ":\n" << electron;
  }

  if(electron.pt() < min_pt_)
  {
    if(debug_)
    {
      std::cout << "FAILS pT >= " << min_pt_ << " tight cut\n";
    }
    return false;
  }
  if(electron.absEta() > max_absEta_)
  {
    if(debug_)
    {
      std::cout << "FAILS abs(eta) <= " << max_absEta_ << " tight cut\n";
    }
    return false;
  }
  if(std::fabs(electron.dxy()) > max_dxy_)
  {
    if(debug_)
    {
      std::cout << "FAILS abs(dxy) <= " << max_dxy_ << " tight cut\n";
    }
    return false;
  }
  if(std::fabs(electron.dz()) > max_dz_)
  {
    if(debug_)
    {
      std::cout << "FAILS max(dz) <= " << max_dz_ << " tight cut\n";
    }
    return false;
  }
  if(electron.relIso() > max_relIso_)
  {
    if(debug_)
    {
      std::cout << "FAILS relIso <= " << max_relIso_ << " tight cut\n";
    }
    return false;
  }
  if(electron.sip3d() > max_sip3d_)
  {
    if(debug_)
    {
      std::cout << "FAILS sip3d <= " << max_sip3d_ << " tight cut\n";
    }
    return false;
  }
  if(electron.jetBtagCSV() > max_jetBtagCSV_)
  {
    if(debug_)
    {
      std::cout << "FAILS jetBtagCSV <= " << max_jetBtagCSV_ << " tight cut\n";
    }
    return false;
  }
  if(electron.nLostHits() > max_nLostHits_)
  {
    if(debug_)
    {
      std::cout << "FAILS nLostHits <= " << max_nLostHits_ << " tight cut\n";
    }
    return false;
  }
  if(apply_conversionVeto_ && ! electron.passesConversionVeto())
  {
    if(debug_)
    {
      std::cout << "FAILS conversion veto\n";
    }
    return false;
  }
  if(electron.mvaRawTTH() < min_mvaTTH_)
  {
    if(debug_)
    {
      std::cout << "FAILS mvaTTH >= " << min_mvaTTH_ << " tight cut\n";
    }
    return false;
  }

  if(! electron.mvaRawPOG_WP(mvaPOGwp_))
  {
    if(debug_)
    {
      std::cout << "FAILS mvaPOG = " << as_integer(mvaPOGwp_) << " tight cut\n";
    }
    return false;
  }

  // extra cuts for electrons passing pT threshold of single electron trigger,
  // as explained in section 3.3.4 of AN-2015/321
  if(apply_offline_e_trigger_cuts_ && electron.pt() >= min_pt_trig_)
  {
    const int idxBin = electron.absEta() <= binning_absEta_[0] ? 0 :
                      (electron.absEta() <= binning_absEta_[1] ? 1 : 2)
    ;

    if(electron.sigmaEtaEta() > max_sigmaEtaEta_trig_[idxBin])
    {
      if(debug_)
      {
        std::cout << "FAILS sigmaEtaEta <= " << max_sigmaEtaEta_trig_[idxBin] << " tight cut\n";
      }
      return false;
    }
    if(electron.HoE() > max_HoE_trig_[idxBin])
    {
      if(debug_)
      {
        std::cout << "FAILS HoE <= " << max_HoE_trig_[idxBin] << " tight cut\n";
      }
      return false;
    }
    if(std::fabs(electron.deltaEta()) > max_deltaEta_trig_[idxBin])
    {
      if(debug_)
      {
        std::cout << "FAILS deltaEta <= " << max_deltaEta_trig_[idxBin] << " tight cut\n";
      }
      return false;
    }
    if(std::fabs(electron.deltaPhi()) > max_deltaPhi_trig_[idxBin])
    {
      if(debug_)
      {
        std::cout << "FAILS deltaPhi <= " << max_deltaPhi_trig_[idxBin] << " tight cut\n";
      }
      return false;
    }
    if(! (electron.OoEminusOoP() >= min_OoEminusOoP_trig_ &&
          electron.OoEminusOoP() <= max_OoEminusOoP_trig_[idxBin]))
    {
      if(debug_)
      {
        std::cout << "FAILS " << min_OoEminusOoP_trig_ << " <= OoEminusOoP <= "
                              << max_OoEminusOoP_trig_[idxBin] << " tight cut\n";
      }
      return false;
    }
  }

  // electron passes all cuts
  if(set_selection_flags_)
  {
    electron.set_isTight();
  }
  return true;
}

RecoElectronCollectionSelectorTight::RecoElectronCollectionSelectorTight(int era,
                                                                         int index,
                                                                         bool debug,
                                                                         bool set_selection_flags)
  : ParticleCollectionSelector<RecoElectron, RecoElectronSelectorTight>(era, index, debug)
{
  selector_.set_selection_flags(set_selection_flags);
}

void
RecoElectronCollectionSelectorTight::enable_offline_e_trigger_cuts()
{
  selector_.enable_offline_e_trigger_cuts();
}

void
RecoElectronCollectionSelectorTight::disable_offline_e_trigger_cuts()
{
  selector_.disable_offline_e_trigger_cuts();
}

// enable/disable photon conversion veto
void
RecoElectronCollectionSelectorTight::enable_conversionVeto()
{
  selector_.enable_conversionVeto();
}

void
RecoElectronCollectionSelectorTight::disable_conversionVeto()
{
  selector_.disable_conversionVeto();
}
