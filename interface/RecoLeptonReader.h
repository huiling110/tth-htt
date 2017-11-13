#ifndef tthAnalysis_HiggsToTauTau_RecoLeptonReader_h
#define tthAnalysis_HiggsToTauTau_RecoLeptonReader_h

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTauReader.h" // GenHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTau.h" // GenHadTau
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h" // GenJetReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/ReaderBase.h" // ReaderBase

#include <Rtypes.h> // Int_t, Float_t
#include <TTree.h> // TTree

#include <string>
#include <vector>
#include <map>

class RecoLeptonReader
  : public ReaderBase
{
 public:
  RecoLeptonReader(bool readGenMatching = false);
  RecoLeptonReader(const std::string& branchName_num, const std::string& branchName_obj, bool readGenMatching = false);
  ~RecoLeptonReader();

  /**
   * @brief Call tree->SetBranchAddress for all lepton branches common to RecoElectrons and RecoMuons
   */
  void setBranchAddresses(TTree* tree) override;

  friend class RecoElectronReader;
  friend class RecoMuonReader;

 protected:
 /**
   * @brief Initialize names of branches to be read from tree
   */
  void setBranchNames();

  const int max_nLeptons_;
  std::string branchName_num_;
  std::string branchName_obj_;

  /**
   * @brief Read branches containing information on matching of RecoElectrons and RecoMuons
   *        to generator level electrons, muons, hadronic taus, and jets from tree
   *        and add this information to collection of RecoElectron and RecoMuon objects given as function argument
   */
  template<typename T>
  void readGenMatching(std::vector<T>& leptons) const
  {
    if ( readGenMatching_ ) {
      assert(genLeptonReader_ && genHadTauReader_ && genJetReader_);
      size_t nLeptons = leptons.size();
      std::vector<GenLepton> matched_genLeptons = genLeptonReader_->read();
      assert(matched_genLeptons.size() == nLeptons);
      std::vector<GenHadTau> matched_genHadTaus = genHadTauReader_->read();
      assert(matched_genHadTaus.size() == nLeptons);
      std::vector<GenJet> matched_genJets = genJetReader_->read();
      assert(matched_genJets.size() == nLeptons);
      for ( size_t idxLepton = 0; idxLepton < nLeptons; ++idxLepton ) {
	T* lepton = &leptons[idxLepton];
	const GenLepton& matched_genLepton = matched_genLeptons[idxLepton];
	if ( matched_genLepton.isValid() ) lepton->set_genLepton(new GenLepton(matched_genLepton), true);
	const GenHadTau& matched_genHadTau = matched_genHadTaus[idxLepton];
	if ( matched_genHadTau.isValid() ) lepton->set_genHadTau(new GenHadTau(matched_genHadTau), true);
	const GenJet& matched_genJet = matched_genJets[idxLepton];
	if ( matched_genJet.isValid() ) lepton->set_genJet(new GenJet(matched_genJet), true);
      }
    }
  }

  GenLeptonReader* genLeptonReader_;
  GenHadTauReader* genHadTauReader_;
  GenJetReader* genJetReader_;
  bool readGenMatching_;

  std::string branchName_pt_;
  std::string branchName_eta_;
  std::string branchName_phi_;
  std::string branchName_mass_;
  std::string branchName_pdgId_;
  std::string branchName_dxy_;
  std::string branchName_dz_;
  std::string branchName_relIso_;
  std::string branchName_chargedHadRelIso03_;
  std::string branchName_miniRelIsoCharged_;
  std::string branchName_sip3d_;
  std::string branchName_mvaRawTTH_;
  std::string branchName_jetPtRatio_;
  std::string branchName_jetBtagCSV_;
  std::string branchName_tightCharge_;
  std::string branchName_charge_;

  UInt_t nLeptons_;
  Float_t* pt_;
  Float_t* eta_;
  Float_t* phi_;
  Float_t* mass_;
  Int_t* pdgId_;
  Float_t* dxy_;
  Float_t* dz_;
  Float_t* relIso_;
  Float_t* chargedHadRelIso03_;
  Float_t* miniRelIsoCharged_;
  Float_t* sip3d_;
  Float_t* mvaRawTTH_;
  Float_t* jetPtRatio_;
  Float_t* jetBtagCSV_;
  Int_t* tightCharge_;
  Int_t* charge_;

  // CV: make sure that only one RecoLeptonReader instance exists for a given branchName,
  //     as ROOT cannot handle multiple TTree::SetBranchAddress calls for the same branch.
  static std::map<std::string, int> numInstances_;
  static std::map<std::string, RecoLeptonReader*> instances_;
};

#endif // tthAnalysis_HiggsToTauTau_RecoLeptonReader_h
