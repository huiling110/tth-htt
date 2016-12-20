#include "tthAnalysis/HiggsToTauTau/interface/ElectronHistManager.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h"

#include <TMath.h>

ElectronHistManager::ElectronHistManager(const edm::ParameterSet& cfg)
  : HistManagerBase(cfg)
{
  idx_ = cfg.getParameter<int>("idx");
}

void ElectronHistManager::bookHistograms(TFileDirectory& dir)
{
  histogram_pt_ = book1D(dir, "pt", "pt", 40, 0., 200.);
  histogram_eta_ = book1D(dir, "eta", "eta", 50, -2.5, +2.5);
  histogram_phi_ = book1D(dir, "phi", "phi", 36, -TMath::Pi(), +TMath::Pi());
  histogram_charge_ = book1D(dir, "charge", "charge", 3, -1.5, +1.5);

  histogram_dxy_ = book1D(dir, "dxy", "dxy", 40, -0.05, +0.05);
  histogram_dz_ = book1D(dir, "dz", "dz", 40, -0.2, +0.2);
  histogram_relIso_ = book1D(dir, "relIso", "relIso", 40, 0., 0.40);
  histogram_sip3d_ = book1D(dir, "sip3d", "sip3d", 40, 0., 8.);
  histogram_mvaRawTTH_ = book1D(dir, "mvaRawTTH", "mvaRawTTH", 40, -1., +1.);
  histogram_jetPtRatio_ = book1D(dir, "jetPtRatio", "jetPtRatio", 24, 0., 1.2);
  histogram_jetBtagCSV_ = book1D(dir, "jetBtagCSV", "jetBtagCSV", 40, 0., 1.);
  histogram_tightCharge_ = book1D(dir, "tightCharge", "tightCharge", 3, -0.5, +2.5);      
  histogram_mvaRawPOG_ = book1D(dir, "mvaRawPOG", "mvaRawPOG", 40, -1., +1.);
  histogram_sigmaEtaEta_ = book1D(dir, "sigmaEtaEta", "sigmaEtaEta", 40, 0., 0.04); 
  histogram_HoE_ = book1D(dir, "HoE", "HoE", 40, 0., 0.20);   
  histogram_deltaEta_ = book1D(dir, "deltaEta", "deltaEta", 40, 0., 0.02);  
  histogram_deltaPhi_ = book1D(dir, "deltaPhi", "deltaPhi", 40, 0., 0.10); 
  histogram_OoEminusOoP_ = book1D(dir, "OoEminusOoP", "OoEminusOoP", 40, -0.05, +0.01);
  histogram_nLostHits_ = book1D(dir, "nLostHits", "nLostHits", 2, -0.5, +1.5);  
  histogram_passesConversionVeto_ = book1D(dir, "passesConversionVeto", "passesConversionVeto", 3, -0.5, +2.5);

  histogram_abs_genPdgId_ = book1D(dir, "abs_genPdgId", "abs_genPdgId", 22, -0.5, +21.5);
  histogram_gen_times_recCharge_ = book1D(dir, "gen_times_recCharge", "gen_times_recCharge", 3, -1.5, +1.5);
}

void ElectronHistManager::fillHistograms(const RecoElectron& electron, double evtWeight)
{
  double evtWeightErr = 0.;
 
  fillWithOverFlow(histogram_pt_, electron.pt(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_eta_, electron.eta(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_phi_, electron.phi(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_charge_, electron.charge(), evtWeight, evtWeightErr);
    
  fillWithOverFlow(histogram_dxy_, electron.dxy(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dz_, electron.dz(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_relIso_, electron.relIso(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_sip3d_, electron.sip3d(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mvaRawTTH_, electron.mvaRawTTH(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_jetPtRatio_, electron.jetPtRatio(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_jetBtagCSV_, electron.jetBtagCSV(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_tightCharge_, electron.tightCharge(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mvaRawPOG_, electron.mvaRawPOG(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_sigmaEtaEta_, electron.sigmaEtaEta(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_HoE_, electron.HoE(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_deltaEta_, electron.deltaEta(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_deltaPhi_, electron.deltaPhi(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_OoEminusOoP_, electron.OoEminusOoP(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_nLostHits_, electron.nLostHits(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_passesConversionVeto_, electron.passesConversionVeto(), evtWeight, evtWeightErr);
  
  int abs_genPdgId = 0;
  if      ( electron.genLepton() ) abs_genPdgId = std::abs(electron.genLepton()->pdgId()); // generator level match to electron or muon
  else if ( electron.genHadTau() ) abs_genPdgId = 15; // generator level match to hadronic tau decay 
  else if ( electron.genJet()    ) abs_genPdgId = 21; // generator level match to jet; fill histogram with pdgId of gluon
  else                             abs_genPdgId = 0;  // no match to any generator level particle (reconstructed electron most likely due to pileup)
  fillWithOverFlow(histogram_abs_genPdgId_, abs_genPdgId, evtWeight, evtWeightErr);
  if ( abs_genPdgId == 11 ) {
    fillWithOverFlow(histogram_gen_times_recCharge_, electron.charge()*electron.genLepton()->charge(), evtWeight, evtWeightErr);
  }
}

void ElectronHistManager::fillHistograms(const std::vector<const RecoElectron*>& electron_ptrs, double evtWeight)
{
  size_t numElectrons = electron_ptrs.size();
  for ( size_t idxElectron = 0; idxElectron < numElectrons; ++idxElectron ) {
    const RecoElectron* electron = electron_ptrs[idxElectron];

    if ( idx_ >= 0 && (int)idxElectron != idx_ ) continue;

    fillHistograms(*electron, evtWeight);
  }
}
