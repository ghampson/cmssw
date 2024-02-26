import FWCore.ParameterSet.Config as cms

# This config was generated automatically using generate2021Geometry.py
# If you notice a mistake, please update the generating script, not just this config

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring(
        'Geometry/CMSCommonData/data/materials/2021/v3/materials.xml',
        'Geometry/TrackerCommonData/data/trackermaterial/2021/v2/trackermaterial.xml',
        'Geometry/CMSCommonData/data/rotations.xml',
        'Geometry/CMSCommonData/data/extend/v3/cmsextent.xml',
        'Geometry/CMSCommonData/data/cavernData/2021/v1/cavernData.xml',
        'Geometry/CMSCommonData/data/cms/2021/v3/cms.xml',
        'Geometry/CMSCommonData/data/cmsMother.xml',
        'Geometry/CMSCommonData/data/eta3/etaMax.xml',
        'Geometry/CMSCommonData/data/cmsTracker.xml',
        'Geometry/CMSCommonData/data/caloBase/2017/v1/caloBase.xml',
        'Geometry/CMSCommonData/data/cmsCalo.xml',
        'Geometry/CMSCommonData/data/muonBase/2018/v1/muonBase.xml',
        'Geometry/CMSCommonData/data/cmsMuon.xml',
        'Geometry/CMSCommonData/data/mgnt.xml',
        'Geometry/CMSCommonData/data/beampipe/2021/v1/beampipe.xml',
        'Geometry/CMSCommonData/data/cmsBeam/2021/v1/cmsBeam.xml',
        'Geometry/CMSCommonData/data/muonMB.xml',
        'Geometry/CMSCommonData/data/muonMagnet.xml',
        'Geometry/CMSCommonData/data/cavern/2021/v1/cavern.xml',
        'Geometry/CMSCommonData/data/cavernFloor/2017/v1/cavernFloor.xml',
        'Geometry/TrackerCommonData/data/PhaseI/trackerParameters.xml',
        'Geometry/TrackerCommonData/data/pixfwdMaterials/2021/v3/pixfwdMaterials.xml',
        'Geometry/TrackerCommonData/data/pixfwdCommon.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixfwdCylinder.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixfwdDisks.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v3/pixfwd.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixfwdSupportRingParameters.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixfwdInnerDiskZplus.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixfwdInnerDiskZminus.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixfwdOuterDiskZplus.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixfwdOuterDiskZminus.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixfwdbladeInnerZplus.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixfwdbladeInnerZminus.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixfwdbladeOuterZplus.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixfwdbladeOuterZminus.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v3/pixbarmaterial.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixbarladder.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixbarladderfull0.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixbarladderfull1.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixbarladderfull2.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixbarladderfull3.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixbarlayer.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixbarlayer0.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixbarlayer1.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixbarlayer2.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixbarlayer3.xml',
        'Geometry/TrackerCommonData/data/PhaseI/v2/pixbar.xml',
        'Geometry/TrackerCommonData/data/Run2/trackerpatchpannel.xml',
        'Geometry/TrackerCommonData/data/Run2/trackerpixelnose.xml',
        'Geometry/TrackerCommonData/data/tibtidcommonmaterial/2021/v2/tibtidcommonmaterial.xml',
        'Geometry/TrackerCommonData/data/tibmaterial/2021/v2/tibmaterial.xml',
        'Geometry/TrackerCommonData/data/tibmodpar.xml',
        'Geometry/TrackerCommonData/data/tibmodule0.xml',
        'Geometry/TrackerCommonData/data/tibmodule0a.xml',
        'Geometry/TrackerCommonData/data/tibmodule0b.xml',
        'Geometry/TrackerCommonData/data/tibmodule2.xml',
        'Geometry/TrackerCommonData/data/tibstringpar.xml',
        'Geometry/TrackerCommonData/data/tibstring0ll.xml',
        'Geometry/TrackerCommonData/data/tibstring0lr.xml',
        'Geometry/TrackerCommonData/data/tibstring0ul.xml',
        'Geometry/TrackerCommonData/data/tibstring0ur.xml',
        'Geometry/TrackerCommonData/data/tibstring0.xml',
        'Geometry/TrackerCommonData/data/tibstring1ll.xml',
        'Geometry/TrackerCommonData/data/tibstring1lr.xml',
        'Geometry/TrackerCommonData/data/tibstring1ul.xml',
        'Geometry/TrackerCommonData/data/tibstring1ur.xml',
        'Geometry/TrackerCommonData/data/tibstring1.xml',
        'Geometry/TrackerCommonData/data/tibstring2ll.xml',
        'Geometry/TrackerCommonData/data/tibstring2lr.xml',
        'Geometry/TrackerCommonData/data/tibstring2ul.xml',
        'Geometry/TrackerCommonData/data/tibstring2ur.xml',
        'Geometry/TrackerCommonData/data/tibstring2.xml',
        'Geometry/TrackerCommonData/data/tibstring3ll.xml',
        'Geometry/TrackerCommonData/data/tibstring3lr.xml',
        'Geometry/TrackerCommonData/data/tibstring3ul.xml',
        'Geometry/TrackerCommonData/data/tibstring3ur.xml',
        'Geometry/TrackerCommonData/data/tibstring3.xml',
        'Geometry/TrackerCommonData/data/tiblayerpar.xml',
        'Geometry/TrackerCommonData/data/tiblayer0.xml',
        'Geometry/TrackerCommonData/data/tiblayer1.xml',
        'Geometry/TrackerCommonData/data/tiblayer2.xml',
        'Geometry/TrackerCommonData/data/tiblayer3.xml',
        'Geometry/TrackerCommonData/data/tib.xml',
        'Geometry/TrackerCommonData/data/tidmaterial/2021/v2/tidmaterial.xml',
        'Geometry/TrackerCommonData/data/tidmodpar.xml',
        'Geometry/TrackerCommonData/data/tidmodule0.xml',
        'Geometry/TrackerCommonData/data/tidmodule0r.xml',
        'Geometry/TrackerCommonData/data/tidmodule0l.xml',
        'Geometry/TrackerCommonData/data/tidmodule1.xml',
        'Geometry/TrackerCommonData/data/tidmodule1r.xml',
        'Geometry/TrackerCommonData/data/tidmodule1l.xml',
        'Geometry/TrackerCommonData/data/tidmodule2.xml',
        'Geometry/TrackerCommonData/data/tidringpar.xml',
        'Geometry/TrackerCommonData/data/tidring0.xml',
        'Geometry/TrackerCommonData/data/tidring0f.xml',
        'Geometry/TrackerCommonData/data/tidring0b.xml',
        'Geometry/TrackerCommonData/data/tidring1.xml',
        'Geometry/TrackerCommonData/data/tidring1f.xml',
        'Geometry/TrackerCommonData/data/tidring1b.xml',
        'Geometry/TrackerCommonData/data/tidring2.xml',
        'Geometry/TrackerCommonData/data/tid.xml',
        'Geometry/TrackerCommonData/data/tidf.xml',
        'Geometry/TrackerCommonData/data/tidb.xml',
        'Geometry/TrackerCommonData/data/tibtidservices.xml',
        'Geometry/TrackerCommonData/data/tibtidservicesf.xml',
        'Geometry/TrackerCommonData/data/tibtidservicesb.xml',
        'Geometry/TrackerCommonData/data/tobmaterial/2021/v2/tobmaterial.xml',
        'Geometry/TrackerCommonData/data/tobmodpar.xml',
        'Geometry/TrackerCommonData/data/tobmodule0.xml',
        'Geometry/TrackerCommonData/data/tobmodule2.xml',
        'Geometry/TrackerCommonData/data/tobmodule4.xml',
        'Geometry/TrackerCommonData/data/tobrodpar.xml',
        'Geometry/TrackerCommonData/data/tobrod0c.xml',
        'Geometry/TrackerCommonData/data/tobrod0l.xml',
        'Geometry/TrackerCommonData/data/tobrod0h.xml',
        'Geometry/TrackerCommonData/data/tobrod0.xml',
        'Geometry/TrackerCommonData/data/tobrod1l.xml',
        'Geometry/TrackerCommonData/data/tobrod1h.xml',
        'Geometry/TrackerCommonData/data/tobrod1.xml',
        'Geometry/TrackerCommonData/data/tobrod2c.xml',
        'Geometry/TrackerCommonData/data/tobrod2l.xml',
        'Geometry/TrackerCommonData/data/tobrod2h.xml',
        'Geometry/TrackerCommonData/data/tobrod2.xml',
        'Geometry/TrackerCommonData/data/tobrod3l.xml',
        'Geometry/TrackerCommonData/data/tobrod3h.xml',
        'Geometry/TrackerCommonData/data/tobrod3.xml',
        'Geometry/TrackerCommonData/data/tobrod4c.xml',
        'Geometry/TrackerCommonData/data/tobrod4l.xml',
        'Geometry/TrackerCommonData/data/tobrod4h.xml',
        'Geometry/TrackerCommonData/data/tobrod4.xml',
        'Geometry/TrackerCommonData/data/tobrod5l.xml',
        'Geometry/TrackerCommonData/data/tobrod5h.xml',
        'Geometry/TrackerCommonData/data/tobrod5.xml',
        'Geometry/TrackerCommonData/data/tob/v3/tob.xml',
        'Geometry/TrackerCommonData/data/tecmaterial/2021/v1/tecmaterial.xml',
        'Geometry/TrackerCommonData/data/tecmodpar.xml',
        'Geometry/TrackerCommonData/data/tecmodule0.xml',
        'Geometry/TrackerCommonData/data/tecmodule0r.xml',
        'Geometry/TrackerCommonData/data/tecmodule0s.xml',
        'Geometry/TrackerCommonData/data/tecmodule1.xml',
        'Geometry/TrackerCommonData/data/tecmodule1r.xml',
        'Geometry/TrackerCommonData/data/tecmodule1s.xml',
        'Geometry/TrackerCommonData/data/tecmodule2.xml',
        'Geometry/TrackerCommonData/data/tecmodule3.xml',
        'Geometry/TrackerCommonData/data/tecmodule4.xml',
        'Geometry/TrackerCommonData/data/tecmodule4r.xml',
        'Geometry/TrackerCommonData/data/tecmodule4s.xml',
        'Geometry/TrackerCommonData/data/tecmodule5.xml',
        'Geometry/TrackerCommonData/data/tecmodule6.xml',
        'Geometry/TrackerCommonData/data/tecpetpar.xml',
        'Geometry/TrackerCommonData/data/tecring0.xml',
        'Geometry/TrackerCommonData/data/tecring1.xml',
        'Geometry/TrackerCommonData/data/tecring2.xml',
        'Geometry/TrackerCommonData/data/tecring3.xml',
        'Geometry/TrackerCommonData/data/tecring4.xml',
        'Geometry/TrackerCommonData/data/tecring5.xml',
        'Geometry/TrackerCommonData/data/tecring6.xml',
        'Geometry/TrackerCommonData/data/tecring0f.xml',
        'Geometry/TrackerCommonData/data/tecring1f.xml',
        'Geometry/TrackerCommonData/data/tecring2f.xml',
        'Geometry/TrackerCommonData/data/tecring3f.xml',
        'Geometry/TrackerCommonData/data/tecring4f.xml',
        'Geometry/TrackerCommonData/data/tecring5f.xml',
        'Geometry/TrackerCommonData/data/tecring6f.xml',
        'Geometry/TrackerCommonData/data/tecring0b.xml',
        'Geometry/TrackerCommonData/data/tecring1b.xml',
        'Geometry/TrackerCommonData/data/tecring2b.xml',
        'Geometry/TrackerCommonData/data/tecring3b.xml',
        'Geometry/TrackerCommonData/data/tecring4b.xml',
        'Geometry/TrackerCommonData/data/tecring5b.xml',
        'Geometry/TrackerCommonData/data/tecring6b.xml',
        'Geometry/TrackerCommonData/data/tecpetalf.xml',
        'Geometry/TrackerCommonData/data/tecpetalb.xml',
        'Geometry/TrackerCommonData/data/tecpetal0.xml',
        'Geometry/TrackerCommonData/data/tecpetal0f.xml',
        'Geometry/TrackerCommonData/data/tecpetal0b.xml',
        'Geometry/TrackerCommonData/data/tecpetal3.xml',
        'Geometry/TrackerCommonData/data/tecpetal3f.xml',
        'Geometry/TrackerCommonData/data/tecpetal3b.xml',
        'Geometry/TrackerCommonData/data/tecpetal6f.xml',
        'Geometry/TrackerCommonData/data/tecpetal6b.xml',
        'Geometry/TrackerCommonData/data/tecpetal8f.xml',
        'Geometry/TrackerCommonData/data/tecpetal8b.xml',
        'Geometry/TrackerCommonData/data/tecwheel/2021/v1/tecwheel.xml',
        'Geometry/TrackerCommonData/data/tecwheela.xml',
        'Geometry/TrackerCommonData/data/tecwheelb.xml',
        'Geometry/TrackerCommonData/data/tecwheelc.xml',
        'Geometry/TrackerCommonData/data/tecwheeld.xml',
        'Geometry/TrackerCommonData/data/tecwheel6.xml',
        'Geometry/TrackerCommonData/data/tecservices.xml',
        'Geometry/TrackerCommonData/data/tecbackplate.xml',
        'Geometry/TrackerCommonData/data/tec.xml',
        'Geometry/TrackerCommonData/data/Run2/tracker.xml',
        'Geometry/TrackerCommonData/data/trackerpixbar.xml',
        'Geometry/TrackerCommonData/data/PhaseI/trackerpixfwd.xml',
        'Geometry/TrackerCommonData/data/trackertibtidservices.xml',
        'Geometry/TrackerCommonData/data/trackertib.xml',
        'Geometry/TrackerCommonData/data/trackertid.xml',
        'Geometry/TrackerCommonData/data/trackertob.xml',
        'Geometry/TrackerCommonData/data/trackertec.xml',
        'Geometry/TrackerCommonData/data/v2/trackerbulkhead.xml',
        'Geometry/TrackerCommonData/data/trackerother.xml',
        'Geometry/TrackerCommonData/data/PhaseI/trackerStructureTopology.xml',
        'Geometry/TrackerSimData/data/PhaseI/trackersens.xml',
        'Geometry/TrackerRecoData/data/PhaseI/v1/trackerRecoMaterial.xml',
        'SimTracker/TrackerMaterialAnalysis/data/trackingMaterialGroups_ForPhaseI/v1/trackingMaterialGroups_ForPhaseI.xml',
        'Geometry/TrackerSimData/data/PhaseI/trackerProdCuts.xml',
        'Geometry/TrackerSimData/data/trackerProdCutsBEAM.xml',
        'Geometry/EcalCommonData/data/ebcon/2021/v1/ebcon.xml',
        'Geometry/EcalCommonData/data/eecon.xml',
        'Geometry/EcalCommonData/data/escon.xml',
        'Geometry/EcalCommonData/data/eregalgo/2017/v1/eregalgo.xml',
        'Geometry/EcalCommonData/data/ebalgo.xml',
        'Geometry/EcalCommonData/data/ebrot.xml',
        'Geometry/EcalCommonData/data/eefixed/2021/v1/eefixed.xml',
        'Geometry/EcalCommonData/data/eehier.xml',
        'Geometry/EcalCommonData/data/eealgo.xml',
        'Geometry/EcalCommonData/data/esalgo.xml',
        'Geometry/EcalCommonData/data/eeF.xml',
        'Geometry/EcalCommonData/data/eeB.xml',
        'Geometry/EcalCommonData/data/ectkcable.xml',
        'Geometry/HcalCommonData/data/hcalrotations.xml',
        'Geometry/HcalCommonData/data/hcal/PhaseI/hcalalgo.xml',
        'Geometry/HcalCommonData/data/hcalcablealgo.xml',
        'Geometry/HcalCommonData/data/hcalbarrelalgo.xml',
        'Geometry/HcalCommonData/data/hcalendcap/PhaseI/hcalendcapalgo.xml',
        'Geometry/HcalCommonData/data/hcalouteralgo/v1/hcalouteralgo.xml',
        'Geometry/HcalCommonData/data/hcalforwardalgo.xml',
        'Geometry/HcalCommonData/data/average/hcalforwardmaterial.xml',
        'Geometry/HcalCommonData/data/hcalSimNumbering/2021/v1/hcalSimNumbering.xml',
        'Geometry/HcalCommonData/data/hcalRecNumbering/2021/v1/hcalRecNumbering.xml',
        'Geometry/MuonCommonData/data/mbCommon/2021/v2/mbCommon.xml',
        'Geometry/MuonCommonData/data/mb1/2021/v1/mb1.xml',
        'Geometry/MuonCommonData/data/mb2/2021/v1/mb2.xml',
        'Geometry/MuonCommonData/data/mb3/2021/v1/mb3.xml',
        'Geometry/MuonCommonData/data/mb4/2015/v2/mb4.xml',
        'Geometry/MuonCommonData/data/mb4Shield/2021/v1/mb4Shield.xml',
        'Geometry/MuonCommonData/data/muonYoke/2021/v5/muonYoke.xml',
        'Geometry/MuonCommonData/data/mf/2021/v3/mf.xml',
        'Geometry/MuonCommonData/data/rpcf/2024/v1/rpcf.xml',
        'Geometry/MuonCommonData/data/gemf/TDR_BaseLine/gemf.xml',
        'Geometry/MuonCommonData/data/gem11/TDR_BaseLine/gem11.xml',
        'Geometry/MuonCommonData/data/gem21/2024/v1/gem21.xml',
        'Geometry/MuonCommonData/data/csc/2021/v3/csc.xml',
        'Geometry/MuonCommonData/data/mfshield/2017/v2/mfshield.xml',
    )+
    cms.vstring(
        'Geometry/MuonCommonData/data/muonNumbering/2024/v1/muonNumbering.xml',
        'Geometry/ForwardCommonData/data/forward/2021/v1/forward.xml',
        'Geometry/ForwardCommonData/data/totemt2/2021/v1/totemt2.xml',
        'Geometry/ForwardCommonData/data/forwardshield/2021/v1/forwardshield.xml',
        'Geometry/ForwardCommonData/data/bhm.xml',
        'Geometry/ForwardCommonData/data/pltbcm/2021/v1/pltbcm.xml',
        'Geometry/ForwardCommonData/data/bcm1f/2021/v1/bcm1f.xml',
        'Geometry/ForwardCommonData/data/plt/2021/v1/plt.xml',
        'Geometry/ForwardCommonData/data/zdcmaterials/2021/v1/zdcmaterials.xml',
        'Geometry/ForwardCommonData/data/lumimaterials.xml',
        'Geometry/ForwardCommonData/data/zdcrotations.xml',
        'Geometry/ForwardCommonData/data/lumirotations.xml',
        'Geometry/ForwardCommonData/data/zdc/2021/v3/zdc.xml',
        'Geometry/ForwardCommonData/data/rpd/2021/v1/rpd.xml',
        'Geometry/ForwardCommonData/data/cmszdc.xml',
        'Geometry/VeryForwardData/data/RP_Box.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_000.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_001.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_002.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_003.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_004.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_005.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_020.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_021.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_022.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_023.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_024.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_025.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_100.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_101.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_102.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_103.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_104.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_105.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_120.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_121.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_122.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_123.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_124.xml',
        'Geometry/VeryForwardData/data/RP_Box/v3/RP_Box_125.xml',
        'Geometry/VeryForwardData/data/RP_Hybrid/v2/RP_Hybrid.xml',
        'Geometry/VeryForwardData/data/RP_Materials/v5/RP_Materials.xml',
        'Geometry/VeryForwardData/data/RP_Transformations.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_000.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_001.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_002.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_004.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_005.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_020.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_021.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_024.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_025.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_100.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_101.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_102.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_104.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_105.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_120.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_121.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_124.xml',
        'Geometry/VeryForwardData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_125.xml',
        'Geometry/VeryForwardData/data/RP_Device/v1/RP_Device.xml',
        'Geometry/VeryForwardData/data/RP_Vertical_Device/2021/Simu/v2/RP_Vertical_Device.xml',
        'Geometry/VeryForwardData/data/RP_Horizontal_Device/2021/Simu/v2/RP_Horizontal_Device.xml',
        'Geometry/VeryForwardData/data/CTPPS_2021/Stations/Simu/v3/CTPPS_220_Right_Station.xml',
        'Geometry/VeryForwardData/data/CTPPS_2021/Stations/Simu/v3/CTPPS_220_Left_Station.xml',
        'Geometry/VeryForwardData/data/CTPPS_2021/Stations/Simu/v3/CTPPS_210_Right_Station.xml',
        'Geometry/VeryForwardData/data/CTPPS_2021/Stations/Simu/v3/CTPPS_210_Left_Station.xml',
        'Geometry/VeryForwardData/data/CTPPS_2021/Stations/Simu/v3/CTPPS_Stations_Assembly.xml',
        'Geometry/VeryForwardData/data/CTPPS_2021/Cuts_Per_Region/Simu/v1/CTPPS_Cuts_Per_Region.xml',
        'Geometry/VeryForwardData/data/RP_Sensitive_Dets.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Transformations.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Parameters.xml',
        'Geometry/VeryForwardData/data/CTPPS_Timing_Station_Parameters.xml',
        'Geometry/VeryForwardData/data/CTPPS_Timing_Horizontal_Pot/v2/CTPPS_Timing_Horizontal_Pot.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern1_Segment1.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern2_Segment1.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern2_Segment2.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern3_Segment1.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern3_Segment2.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern3_Segment3.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern3_Segment4.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern4_Segment1.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern4_Segment2.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern4_Segment3.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern4_Segment4.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Segments/CTPPS_Diamond_Pattern4_Segment5.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_2021/CTPPS_Diamond_Planes/CTPPS_Diamond_Plane1.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_2021/CTPPS_Diamond_Planes/CTPPS_Diamond_Plane2.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_2021/CTPPS_Diamond_Planes/CTPPS_Diamond_Plane3.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_2021/CTPPS_Diamond_Planes/CTPPS_Diamond_Plane4.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_2021/CTPPS_Diamond_Detector_Assembly/v1/CTPPS_Diamond_Detector_Assembly.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_2021/Simu/v1/CTPPS_Detectors_Assembly_022.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_2021/Simu/v1/CTPPS_Detectors_Assembly_122.xml',
        'Geometry/VeryForwardData/data/CTPPS_Diamond_Sensitive_Dets_TimingHits.xml',
        'Geometry/VeryForwardData/data/CTPPS_Pixel_2021/Modules/v3/PPS_Pixel_Module_2x2_Run3.xml',
        'Geometry/VeryForwardData/data/CTPPS_Pixel_2021/Modules/v2/PPS_Pixel_Sens.xml',
        'Geometry/VeryForwardData/data/CTPPS_Pixel_2021/Assembly/v2/CTPPS_Pixel_Assembly_Box_Real_003.xml',
        'Geometry/VeryForwardData/data/CTPPS_Pixel_2021/Assembly/v2/CTPPS_Pixel_Assembly_Box_Real_023.xml',
        'Geometry/VeryForwardData/data/CTPPS_Pixel_2021/Assembly/v2/CTPPS_Pixel_Assembly_Box_Real_103.xml',
        'Geometry/VeryForwardData/data/CTPPS_Pixel_2021/Assembly/v2/CTPPS_Pixel_Assembly_Box_Real_123.xml',
        'Geometry/VeryForwardData/data/CTPPS_2021/RP_Dist_Beam_Cent/Simu/v1/RP_Dist_Beam_Cent.xml',
        'Geometry/EcalSimData/data/ecalsens.xml',
        'Geometry/HcalCommonData/data/hcalsens/2021/v2/hcalsenspmf.xml',
        'Geometry/HcalSimData/data/hf.xml',
        'Geometry/HcalSimData/data/hfpmt.xml',
        'Geometry/HcalSimData/data/hffibrebundle.xml',
        'Geometry/HcalSimData/data/CaloUtil/2021/v1/CaloUtil.xml',
        'Geometry/MuonSimData/data/muonSens/2021/v4/muonSens.xml',
        'Geometry/DTGeometryBuilder/data/dtSpecsFilter/2021/v1/dtSpecsFilter.xml',
        'Geometry/CSCGeometryBuilder/data/cscSpecsFilter.xml',
        'Geometry/CSCGeometryBuilder/data/cscSpecs.xml',
        'Geometry/RPCGeometryBuilder/data/2021/v1/RPCSpecs.xml',
        'Geometry/GEMGeometryBuilder/data/GEMSpecsFilter/2021/v2/GEMSpecsFilter.xml',
        'Geometry/GEMGeometryBuilder/data/GEMSpecs/2021/v2/GEMSpecs.xml',
        'Geometry/ForwardSimData/data/totemsensT2/2021/totemsensT2.xml',
        'Geometry/ForwardCommonData/data/bhmsens.xml',
        'Geometry/ForwardSimData/data/pltsens.xml',
        'Geometry/ForwardSimData/data/bcm1fsens.xml',
        'Geometry/ForwardSimData/data/zdcsens/2021/v1/zdcsens.xml',
        'Geometry/HcalSimData/data/HcalProdCuts/2021/v2/HcalProdCuts.xml',
        'Geometry/EcalSimData/data/EcalProdCuts.xml',
        'Geometry/EcalSimData/data/ESProdCuts.xml',
        'Geometry/MuonSimData/data/muonProdCuts/2021/v3/muonProdCuts.xml',
        'Geometry/ForwardSimData/data/ForwardShieldProdCuts.xml',
        'Geometry/ForwardSimData/data/bhmProdCuts/2021/v1/bhmProdCuts.xml',
        'Geometry/ForwardSimData/data/zdcProdCuts/2021/v3/zdcProdCuts.xml',
        'Geometry/CMSCommonData/data/FieldParameters.xml',
    ),
    rootNodeName = cms.string('cms:OCMS')
)
