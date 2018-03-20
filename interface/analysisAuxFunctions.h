#ifndef tthAnalysis_HiggsToTauTau_analysisAuxFunctions_h
#define tthAnalysis_HiggsToTauTau_analysisAuxFunctions_h

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()

#include <DataFormats/Math/interface/deltaR.h> // deltaR()
#include <DataFormats/Math/interface/LorentzVector.h> // math::PtEtaPhiMLorentzVector

#include <vector> // std::vector<>
#include <map> // std::map<,>
#include <algorithm> // std::copy_n()

// forward declarations
class Particle;
class RecoLepton;
class RecoJet;
class RecoHadTau;
class RecoMuon;
class RecoElectron;

//--- declare constants
const double z_mass   = 91.1876;
const double z_window = 10.;
const double met_coef =  0.00397;
const double mht_coef =  0.00265;

//--- declare data-taking periods
enum
{
  kEra_2017
};

//--- declare systematic uncertainties on data/MC corrections for
//    b-tagging efficiency and mistag rates
enum
{
  kBtag_central,

  kBtag_hfUp,       kBtag_hfDown,
  kBtag_hfStats1Up, kBtag_hfStats1Down,
  kBtag_hfStats2Up, kBtag_hfStats2Down,

  kBtag_lfUp,       kBtag_lfDown,
  kBtag_lfStats1Up, kBtag_lfStats1Down,
  kBtag_lfStats2Up, kBtag_lfStats2Down,

  kBtag_cErr1Up, kBtag_cErr1Down,
  kBtag_cErr2Up, kBtag_cErr2Down,

  kBtag_jesUp, kBtag_jesDown
};

//--- declare selection criteria for leptons and hadronic taus
enum { kLoose, kFakeable, kTight };

//--- declare b-tagging working points

enum class BtagWP { kLoose, kMedium, kTight };

//--- source: https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
const std::map<BtagWP, double> BtagWP_CSV_2016 =
{
  { BtagWP::kLoose,  0.5426 },
  { BtagWP::kMedium, 0.8484 },
  { BtagWP::kTight,  0.9535 },
};

//--- source: https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
const std::map<BtagWP, double> BtagWP_CSVv2_2017 =
{
  { BtagWP::kLoose,  0.5803 },
  { BtagWP::kMedium, 0.8838 },
  { BtagWP::kTight,  0.9693 },
};

//--- source: https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
const std::map<BtagWP, double> BtagWP_deepCSV_2017 =
{
  { BtagWP::kLoose,  0.1522 },
  { BtagWP::kMedium, 0.4941 },
  { BtagWP::kTight,  0.8001 },
};

double
get_BtagWP(int era,
           BtagWP wp);

//--- selector class
template <typename LeptonType>
std::vector<LeptonType>
selectObjects(int objectSelection,
              const std::vector<LeptonType> & preselObjects,
              const std::vector<LeptonType> & fakeableObjects,
              const std::vector<LeptonType> & tightObjects)
{
  switch(objectSelection)
  {
    case kLoose:    return preselObjects;
    case kFakeable: return fakeableObjects;
    case kTight:    return tightObjects;
    default:        throw cmsException(__func__) << "Invalid selection: " << objectSelection;
  }
}

int
get_selection(const std::string & selectionString);

int
get_era(const std::string & eraString);

//--- define the tau MVA ID WPs
const std::map<std::string, int>
id_mva_dr03_map = {
  { "dR03mvaVVLoose", 1 }, // custom WP with 95% signal efficiency, computed in RecoHadTauReader
  { "dR03mvaVLoose",  2 },
  { "dR03mvaLoose",   3 },
  { "dR03mvaMedium",  4 },
  { "dR03mvaTight",   5 },
  { "dR03mvaVTight",  6 },
  { "dR03mvaVVTight", 7 }
};

const std::map<std::string, int>
id_mva_dr05_map = {
  { "dR05isoLoose",  1 },
  { "dR05isoMedium", 2 },
  { "dR05isoTight",  3 }
};

/**
 * @brief Auxiliary function used for sorting leptons by decreasing pT
 * @param Given pair of leptons
 * @return True, if first lepton has higher pT; false if second lepton has higher pT
 */
bool
isHigherPt(const Particle * particle1,
           const Particle * particle2);

/**
 * @brief Auxiliary function used for sorting leptons by decreasing cone pT
 * @param Given pair of leptons
 * @return True, if first lepton has higher cone pT; false if second lepton has higher cone pT
 */
bool
isHigherConePt(const RecoLepton * particle1,
               const RecoLepton * particle2);

/**
 * @brief Auxiliary function for sorting a collection of RecoJet pointers
 *        by their b-tagging CSV score
 * @param jet1 The first jet
 * @param jet2 The second jet
 * @return True, if the 1st jet has higher CSV score
 */
bool
isHigherCSV(const RecoJet * jet1,
            const RecoJet * jet2);

/**
 * @brief Auxiliary function for checking if leptons passing fake-able lepton selection
 *        pass tight lepton identification criteria also
 */
template <typename Tfakeable, typename Ttight>
bool
isMatched(const Tfakeable & fakeableLepton,
          const std::vector<Ttight *> & tightLeptons,
          double dRmax = 1.e-2)
{
  for(const Ttight * tightLepton: tightLeptons)
  {
    const double dR = deltaR(
      fakeableLepton.eta(), fakeableLepton.phi(), tightLepton->eta(), tightLepton->phi()
    );
    if(dR < dRmax)
    {
      return true; // found match
    }
  }
  return false; // no match found
}

/**
 * @brief Return branchName to read weights that need to be applied, per jet, to MC events
 *       in order to correct for data/MC differences in b-tagging efficiency and mistag rates
 */
int
getBTagWeight_option(const std::string & central_or_shift);

std::string
getBranchName_bTagWeight(const std::string & default_collectionName,
                         int era,
                         int central_or_shift);

/**
 * @brief Return branch name to read MEt pt and phi
 */
std::string
getBranchName_MEt(int era,
                  const std::string & default_branchName,
                  int central_or_shift);

/**
 * @brief Return first N objects from collection given as function argument. In case the input
 *        collection contains fewer than N objects, the whole input collection is returned
 */
template <typename T>
std::vector<T>
pickFirstNobjects(const std::vector<T> & objects_input,
                  std::size_t N)
{
  const std::size_t N_input = std::min(objects_input.size(), N);
  std::vector<T> objects_output;
  std::copy_n(objects_input.begin(), N_input, std::back_inserter(objects_output));
  return objects_output;
}

int
getHadTau_genPdgId(const RecoHadTau * hadTau);

/**
 * @brief Compute MHT
 */
math::PtEtaPhiMLorentzVector
compMHT(const std::vector<const RecoLepton *> & leptons,
        const std::vector<const RecoHadTau *> & hadTaus,
        const std::vector<const RecoJet *> & jets);

/**
 * @brief Compute linear discriminator based on MET and MHT
 */
double
compMEt_LD(const math::PtEtaPhiMLorentzVector & met_p4,
           const math::PtEtaPhiMLorentzVector & mht_p4);

/**
 * @brief Set flags indicating whether or not lepton passes loose, fakeable and/or tight selection criteria
 */
template <typename T>
void
set_selection_flags(std::vector<const T *> & leptons,
                    int selection)
{
  for(const T * lepton: leptons)
  {
    switch (selection) {
      case kLoose:    lepton->set_isLoose();    break;
      case kFakeable: lepton->set_isFakeable(); break;
      case kTight:    lepton->set_isTight();    break;
      default:        assert(0);
    }
  }
}

/**
 * @brief Build collection of selected leptons by merging collections of selected electrons and selected muons
 */
std::vector<const RecoLepton *>
mergeLeptonCollectionsNoSort(const std::vector<const RecoElectron *> & electrons,
                             const std::vector<const RecoMuon *> & muons);

std::vector<const RecoLepton *>
mergeLeptonCollections(const std::vector<const RecoElectron *> & electrons,
                       const std::vector<const RecoMuon *> & muons);

template <typename T>
std::vector<const RecoLepton *>
mergeLeptonCollections(const std::vector<const RecoElectron *> & electrons,
                       const std::vector<const RecoMuon *> & muons,
                       bool (*sortFunction)(const T *, const T *))
{
  std::vector<const RecoLepton *> leptons = mergeLeptonCollectionsNoSort(electrons, muons);
  std::sort(leptons.begin(), leptons.end(), sortFunction);
  return leptons;
}

template <typename T,
          typename = typename std::enable_if<! std::is_pointer<T>::value>>
void
printCollection(const std::string & collection_name,
                const std::vector<T> & collection)
{
  std::cout << " (#" << collection_name << " = " << collection.size() << ")\n";
  for(std::size_t idx = 0; idx < collection.size(); ++idx)
  {
    std::cout << collection_name << "  #" << idx << ":\n" << collection[idx];
  }
}

template <typename T,
          typename = typename std::enable_if<! std::is_pointer<T>::value>>
void
printCollection(const std::string & collection_name,
                const std::vector<const T *> & collection)
{
  std::cout << " (#" << collection_name << " = " << collection.size() << ")\n";
  for(std::size_t idx = 0; idx < collection.size(); ++idx)
  {
    std::cout << collection_name << "  #" << idx << ":\n" << *(collection[idx]);
  }
}

/**
 * @brief Computes the number of k combinations out of n
 * @param n Number of instances to choose from
 * @param k Length of a single combination
 *
 * Credit to the author of: https://stackoverflow.com/a/9331125
 */
int
nCombinationsK(int n,
               int k);

#endif
