import FWCore.ParameterSet.Config as cms



gemDigiValidation = cms.EDAnalyzer('MuonGEMDigis',
	outputFile = cms.string(''),
	stripLabel= cms.InputTag('simMuonGEMDigis'),
	cscPadLabel = cms.InputTag('simMuonGEMCSCPadDigis'),
	cscCopadLabel = cms.InputTag('simMuonGEMCSCPadDigis','Coincidence') ,
        simInputLabel = cms.untracked.string('g4SimHits'),
	minPt = cms.untracked.double(5.),
	maxEta = cms.untracked.double(2.18),
	minEta = cms.untracked.double(1.55), 
        simTrackMatching = cms.PSet(
            # common
            useCSCChamberTypes = cms.untracked.vint32( 2, ), # by default, only use simhits from ME1/b (CSC type == 2)
            # SimHit matching:
            verboseSimHit = cms.untracked.int32(0),
            simMuOnlyCSC = cms.untracked.bool(True),
            simMuOnlyGEM = cms.untracked.bool(True),
            discardEleHitsCSC = cms.untracked.bool(True),
            discardEleHitsGEM = cms.untracked.bool(True),
            simInputLabel = cms.untracked.string('g4SimHits'),
            # GEM digi matching:
            verboseGEMDigi = cms.untracked.int32(0),
            gemDigiInput = cms.untracked.InputTag("simMuonGEMDigis"),
            gemPadDigiInput = cms.untracked.InputTag("simMuonGEMCSCPadDigis"),
            gemCoPadDigiInput = cms.untracked.InputTag("simMuonGEMCSCPadDigis", "Coincidence"),
            minBXGEM = cms.untracked.int32(-1),
            maxBXGEM = cms.untracked.int32(1),
            matchDeltaStripGEM = cms.untracked.int32(1),
            gemDigiMinEta  = cms.untracked.double(1.55),
            gemDigiMaxEta  = cms.untracked.double(2.18),
            gemDigiMinPt = cms.untracked.double(5.0),
            )
)
