import FWCore.ParameterSet.Config as cms

SiStripDigiToRaw = cms.EDProducer(
    "SiStripDigiToRawModule",
    InputDigis=cms.InputTag('simSiStripDigis', 'ZeroSuppressed'),
    FedReadoutMode = cms.string('ZERO_SUPPRESSED'),
    PacketCode = cms.string('ZERO_SUPPRESSED'),
    UseFedKey = cms.bool(False),
    UseWrongDigiType = cms.bool(False),
    CopyBufferHeader = cms.bool(False),
    RawDataTag = cms.InputTag('rawDataCollector')
    )

from Configuration.ProcessModifiers.premix_stage1_cff import premix_stage1
premix_stage1.toModify(SiStripDigiToRaw, FedReadoutMode = 'PREMIX_RAW', PacketCode="")
