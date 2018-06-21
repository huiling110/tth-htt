import FWCore.ParameterSet.Config as cms

EvtYieldHistManager_2017 = cms.PSet(
    runPeriods = cms.PSet(
        Run2017B = cms.PSet(
            runRange = cms.string("297047~299329"),
            luminosity = cms.double(4.794)
        ),
        Run2017C = cms.PSet(
            runRange = cms.string("299368-302029"),
            luminosity = cms.double(9.631)
        ),
        Run2017D = cms.PSet(
            runRange = cms.string("302030~302663"),
            luminosity = cms.double(4.248)
        ),
        Run2017E = cms.PSet(
            runRange = cms.string("303818~304797"),
            luminosity = cms.double(9.314)
        ),
        Run2017F = cms.PSet(
            runRange = cms.string("305040~306460"),
            luminosity = cms.double(13.539)
        )
    )
)
