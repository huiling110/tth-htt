#ifndef tthAnalysis_HiggsToTauTau_EvtHistManager_4l_h
#define tthAnalysis_HiggsToTauTau_EvtHistManager_4l_h

/** \class EvtHistManager_4l
 *
 * Book and fill histograms for event-level quantities in ttH multilepton analysis
 * in 4l category
 *
 * \author Christian Veelken, Tallin
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

struct EvtHistManager_4l_Input
{
  std::size_t numElectrons;
  std::size_t numMuons;
  std::size_t numJets;
  std::size_t numBJets_loose;
  std::size_t numBJets_medium;
  double mass_4L;
  double mva_4l;
  int ctrl_category;
  double evtWeight;
};

class EvtHistManager_4l
  : public HistManagerBase
{
 public:
  EvtHistManager_4l(const edm::ParameterSet & cfg, bool isControlRegion);
  ~EvtHistManager_4l() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(const EvtHistManager_4l_Input & variables);

  const TH1 *
  getHistogram_EventCounter() const;

  enum { kOption_undefined, kOption_allHistograms, kOption_minimalHistograms };

 private:
  std::vector<std::string> ctrl_cateories_;

  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numJets_;
  TH1 * histogram_numBJets_loose_;
  TH1 * histogram_numBJets_medium_;
  TH1 * histogram_mass_4L_;
  TH1 * histogram_mva_4l_;

  // CV: used to check loss in signal efficiency in case events with high jet and b-jet multiplicity are vetoed
  // to avoid overlap with ttH, H->bb analysis (alternative: ttH, H->bb analysis adds hadronic tau veto)
  TH2 * histogram_numBJets_loose_vs_numJets_;
  TH2 * histogram_numBJets_medium_vs_numJets_;

  TH1 * histogram_ctrl_;

  TH1 * histogram_EventCounter_;
  int option_; // flag to book & fill either full or minimal set of histograms (to reduce memory consumption of hadd jobs)
};

#endif
