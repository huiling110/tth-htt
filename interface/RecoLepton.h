#ifndef tthAnalysis_HiggsToTauTau_RecoLepton_h
#define tthAnalysis_HiggsToTauTau_RecoLepton_h

#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton

class RecoLepton
  : public GenLepton
{
public:
  RecoLepton() = default;
  RecoLepton(Double_t pt,
	     Double_t eta,
	     Double_t phi,
	     Double_t mass,
	     Int_t pdgId,
	     Double_t dxy,
	     Double_t dz,
	     Double_t relIso,
	     Double_t sip3d,
	     Double_t mvaRawTTH,
	     Double_t jetPtRatio,
	     Double_t jetBtagCSV,
	     Int_t tightCharge);

  /**
   * @brief Checks whether a given lepton is an electron by its PDG id
   * @return True if it is an electron; false otherwise
   */
  virtual bool
  is_electron() const { return false; }

  /**
   * @brief Checks whether a given lepton is a muon by its PDG id
   * @return True if it is a muon; false otherwise
   */
  virtual bool
  is_muon() const { return false; }

//--- common observables for electrons and muons
  Double_t dxy_;                        ///< d_{xy}, distance in the transverse plane w.r.t PV
  Double_t dz_;                         ///< d_{z}, distance on the z axis w.r.t PV
  Double_t relIso_;                     ///< relative isolation
  Double_t sip3d_;                      ///< significance of IP
  Double_t mvaRawTTH_;                  ///< raw output of lepton MVA of ttH multilepton analysis
  Double_t jetPtRatio_;                 ///< ratio of lepton pT to pT of nearby jet
  Double_t jetBtagCSV_;                 ///< CSV b-tagging discriminator value of nearby jet
  Int_t tightCharge_;                   ///< Flag indicating if lepton passes (>= 2) or fails (< 2) tight charge requirement
};

#endif // tthAnalysis_HiggsToTauTau_RecoLepton_h

