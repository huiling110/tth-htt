from collections import OrderedDict as OD

# file generated with the following command:
# ./scripts/create_dictionary.py -v -m python/metaDict_2016.py -p /hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples -Zz -N samples_2016

samples_2016 = OD()
samples_2016["/DoubleEG/Run2016B-23Sep2016-v3/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleEG_Run2016B_v3"),
  ("nof_files",                       214),
  ("nof_events",                      143073268),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['2e', '3e']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleEG_Run2016B_v3"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleEG/Run2016C-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleEG_Run2016C_v1"),
  ("nof_files",                       16),
  ("nof_events",                      47677856),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['2e', '3e']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleEG_Run2016C_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleEG/Run2016D-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleEG_Run2016D_v1"),
  ("nof_files",                       26),
  ("nof_events",                      53324960),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['2e', '3e']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleEG_Run2016D_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleEG/Run2016E-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleEG_Run2016E_v1"),
  ("nof_files",                       23),
  ("nof_events",                      49877710),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['2e', '3e']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleEG_Run2016E_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleEG/Run2016F-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleEG_Run2016F_v1"),
  ("nof_files",                       17),
  ("nof_events",                      34577629),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['2e', '3e']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleEG_Run2016F_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleEG/Run2016G-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleEG_Run2016G_v1"),
  ("nof_files",                       39),
  ("nof_events",                      78797031),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['2e', '3e']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleEG_Run2016G_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleEG/Run2016H-PromptReco-v2/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleEG_Run2016H_v2_promptReco"),
  ("nof_files",                       190),
  ("nof_events",                      84344490),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['2e', '3e']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleEG_Run2016H_v2_promptReco"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleEG/Run2016H-PromptReco-v3/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleEG_Run2016H_v3_promptReco"),
  ("nof_files",                       4),
  ("nof_events",                      2146647),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['2e', '3e']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleEG_Run2016H_v3_promptReco"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleMuon/Run2016B-23Sep2016-v3/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleMuon_Run2016B_v3"),
  ("nof_files",                       50),
  ("nof_events",                      82535526),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['2mu', '3mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleMuon_Run2016B_v3"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleMuon/Run2016C-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleMuon_Run2016C_v1"),
  ("nof_files",                       16),
  ("nof_events",                      27934629),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['2mu', '3mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleMuon_Run2016C_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleMuon/Run2016D-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleMuon_Run2016D_v1"),
  ("nof_files",                       26),
  ("nof_events",                      33861745),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['2mu', '3mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleMuon_Run2016D_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleMuon/Run2016E-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleMuon_Run2016E_v1"),
  ("nof_files",                       23),
  ("nof_events",                      28246946),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['2mu', '3mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleMuon_Run2016E_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleMuon/Run2016F-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleMuon_Run2016F_v1"),
  ("nof_files",                       17),
  ("nof_events",                      20329921),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['2mu', '3mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleMuon_Run2016F_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleMuon/Run2016G-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleMuon_Run2016G_v1"),
  ("nof_files",                       39),
  ("nof_events",                      45235604),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['2mu', '3mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleMuon_Run2016G_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleMuon/Run2016H-PromptReco-v2/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleMuon_Run2016H_v2_promptReco"),
  ("nof_files",                       205),
  ("nof_events",                      48093751),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['2mu', '3mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleMuon_Run2016H_v2_promptReco"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DoubleMuon/Run2016H-PromptReco-v3/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "DoubleMuon_Run2016H_v3_promptReco"),
  ("nof_files",                       4),
  ("nof_events",                      1219733),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['2mu', '3mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DoubleMuon_Run2016H_v3_promptReco"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/MuonEG/Run2016B-23Sep2016-v3/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "MuonEG_Run2016B_v3"),
  ("nof_files",                       50),
  ("nof_events",                      32727796),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e1mu', '2e1mu', '1e2mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/MuonEG_Run2016B_v3"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/MuonEG/Run2016C-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "MuonEG_Run2016C_v1"),
  ("nof_files",                       16),
  ("nof_events",                      15405678),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e1mu', '2e1mu', '1e2mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/MuonEG_Run2016C_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/MuonEG/Run2016D-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "MuonEG_Run2016D_v1"),
  ("nof_files",                       108),
  ("nof_events",                      23482352),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e1mu', '2e1mu', '1e2mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/MuonEG_Run2016D_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/MuonEG/Run2016E-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "MuonEG_Run2016E_v1"),
  ("nof_files",                       23),
  ("nof_events",                      22519303),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e1mu', '2e1mu', '1e2mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/MuonEG_Run2016E_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/MuonEG/Run2016F-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "MuonEG_Run2016F_v1"),
  ("nof_files",                       17),
  ("nof_events",                      16002165),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e1mu', '2e1mu', '1e2mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/MuonEG_Run2016F_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/MuonEG/Run2016G-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "MuonEG_Run2016G_v1"),
  ("nof_files",                       39),
  ("nof_events",                      33854612),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['1e1mu', '2e1mu', '1e2mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/MuonEG_Run2016G_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/MuonEG/Run2016H-PromptReco-v2/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "MuonEG_Run2016H_v2_promptReco"),
  ("nof_files",                       144),
  ("nof_events",                      28705853),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['1e1mu', '2e1mu', '1e2mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/MuonEG_Run2016H_v2_promptReco"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/MuonEG/Run2016H-PromptReco-v3/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "MuonEG_Run2016H_v3_promptReco"),
  ("nof_files",                       5),
  ("nof_events",                      770494),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['1e1mu', '2e1mu', '1e2mu']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/MuonEG_Run2016H_v3_promptReco"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleElectron/Run2016B-23Sep2016-v3/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleElectron_Run2016B_v3"),
  ("nof_files",                       150),
  ("nof_events",                      246440440),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e', '1e1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleElectron_Run2016B_v3"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleElectron/Run2016C-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleElectron_Run2016C_v1"),
  ("nof_files",                       47),
  ("nof_events",                      97259854),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e', '1e1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleElectron_Run2016C_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleElectron/Run2016D-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleElectron_Run2016D_v1"),
  ("nof_files",                       76),
  ("nof_events",                      148167727),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e', '1e1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleElectron_Run2016D_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleElectron/Run2016E-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleElectron_Run2016E_v1"),
  ("nof_files",                       68),
  ("nof_events",                      117321545),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e', '1e1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleElectron_Run2016E_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleElectron/Run2016F-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleElectron_Run2016F_v1"),
  ("nof_files",                       17),
  ("nof_events",                      70593532),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e', '1e1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleElectron_Run2016F_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleElectron/Run2016G-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleElectron_Run2016G_v1"),
  ("nof_files",                       39),
  ("nof_events",                      153232788),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['1e', '1e1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleElectron_Run2016G_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleElectron/Run2016H-PromptReco-v2/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleElectron_Run2016H_v2_promptReco"),
  ("nof_files",                       190),
  ("nof_events",                      126863489),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['1e', '1e1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleElectron_Run2016H_v2_promptReco"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleElectron/Run2016H-PromptReco-v3/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleElectron_Run2016H_v3_promptReco"),
  ("nof_files",                       4),
  ("nof_events",                      3191585),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['1e', '1e1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleElectron_Run2016H_v3_promptReco"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleMuon/Run2016B-23Sep2016-v3/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleMuon_Run2016B_v3"),
  ("nof_files",                       148),
  ("nof_events",                      158145722),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1mu', '1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleMuon_Run2016B_v3"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleMuon/Run2016C-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleMuon_Run2016C_v1"),
  ("nof_files",                       47),
  ("nof_events",                      67441308),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1mu', '1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleMuon_Run2016C_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleMuon/Run2016D-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleMuon_Run2016D_v1"),
  ("nof_files",                       26),
  ("nof_events",                      98017996),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1mu', '1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleMuon_Run2016D_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleMuon/Run2016E-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleMuon_Run2016E_v1"),
  ("nof_files",                       68),
  ("nof_events",                      90984718),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1mu', '1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleMuon_Run2016E_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleMuon/Run2016F-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleMuon_Run2016F_v1"),
  ("nof_files",                       17),
  ("nof_events",                      65489554),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1mu', '1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleMuon_Run2016F_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleMuon/Run2016G-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleMuon_Run2016G_v1"),
  ("nof_files",                       39),
  ("nof_events",                      149916849),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['1mu', '1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleMuon_Run2016G_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleMuon/Run2016H-PromptReco-v2/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleMuon_Run2016H_v2_promptReco"),
  ("nof_files",                       205),
  ("nof_events",                      171134793),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['1mu', '1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleMuon_Run2016H_v2_promptReco"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/SingleMuon/Run2016H-PromptReco-v3/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "SingleMuon_Run2016H_v3_promptReco"),
  ("nof_files",                       5),
  ("nof_events",                      4393222),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['1mu', '1tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/SingleMuon_Run2016H_v3_promptReco"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/Tau/Run2016B-23Sep2016-v3/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "Tau_Run2016B_v3"),
  ("nof_files",                       214),
  ("nof_events",                      68727458),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/Tau_Run2016B_v3"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/Tau/Run2016C-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "Tau_Run2016C_v1"),
  ("nof_files",                       68),
  ("nof_events",                      36931473),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/Tau_Run2016C_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/Tau/Run2016D-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "Tau_Run2016D_v1"),
  ("nof_files",                       109),
  ("nof_events",                      56827771),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/Tau_Run2016D_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/Tau/Run2016E-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "Tau_Run2016E_v1"),
  ("nof_files",                       98),
  ("nof_events",                      58348773),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/Tau_Run2016E_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/Tau/Run2016F-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "Tau_Run2016F_v1"),
  ("nof_files",                       70),
  ("nof_events",                      40549716),
  ("use_HIP_mitigation_bTag",         True),
  ("use_HIP_mitigation_mediumMuonId", True),
  ("use_it",                          True),
  ("triggers",                        ['1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/Tau_Run2016F_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/Tau/Run2016G-23Sep2016-v1/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "Tau_Run2016G_v1"),
  ("nof_files",                       39),
  ("nof_events",                      79578661),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/Tau_Run2016G_v1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/Tau/Run2016H-PromptReco-v2/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "Tau_Run2016H_v2_promptReco"),
  ("nof_files",                       152),
  ("nof_events",                      76504267),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/Tau_Run2016H_v2_promptReco"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/Tau/Run2016H-PromptReco-v3/MINIAOD"] = OD([
  ("type",                            "data"),
  ("sample_category",                 "data_obs"),
  ("process_name_specific",           "Tau_Run2016H_v3_promptReco"),
  ("nof_files",                       5),
  ("nof_events",                      1898072),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("triggers",                        ['1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/Tau_Run2016H_v3_promptReco"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "DYJetsToLL_M-10to50"),
  ("nof_files",                       45),
  ("nof_events",                      35233416),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        18610.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DYJetsToLL_M-10to50"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "DYJetsToLL_M-50_ext1"),
  ("nof_files",                       62),
  ("nof_events",                      49002944),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        6025.2),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DYJetsToLL_M-50_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "DYJetsToLL_M-50_ext2"),
  ("nof_files",                       120),
  ("nof_events",                      94911641),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        6025.2),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/DYJetsToLL_M-50_ext2"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "additional_signal_overlap"),
  ("process_name_specific",           "GluGluHToZZTo4L"),
  ("nof_files",                       3),
  ("nof_events",                      999912),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.0119),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/GluGluHToZZTo4L"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "ST_s-channel_4f_leptonDecays"),
  ("nof_files",                       3),
  ("nof_events",                      622688),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        3.68),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/ST_s-channel_4f_leptonDecays"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "ST_t-channel_antitop_4f_inclusiveDecays"),
  ("nof_files",                       98),
  ("nof_events",                      38795360),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        80.95),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/ST_t-channel_antitop_4f_inclusiveDecays"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "ST_t-channel_top_4f_inclusiveDecays"),
  ("nof_files",                       170),
  ("nof_events",                      67073432),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        136.02),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/ST_t-channel_top_4f_inclusiveDecays"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "ST_tW_antitop_5f_inclusiveDecays"),
  ("nof_files",                       18),
  ("nof_events",                      6884378),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        35.6),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/ST_tW_antitop_5f_inclusiveDecays"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "ST_tW_top_5f_inclusiveDecays"),
  ("nof_files",                       18),
  ("nof_events",                      6942671),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        35.6),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/ST_tW_top_5f_inclusiveDecays"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "TGJets_ext1"),
  ("nof_files",                       4),
  ("nof_events",                      306204),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        2.967),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TGJets_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "TGJets"),
  ("nof_files",                       1),
  ("nof_events",                      58022),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        2.967),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TGJets"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "TTGJets_ext1"),
  ("nof_files",                       25),
  ("nof_events",                      3166809),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        3.697),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTGJets_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "TTGJets"),
  ("nof_files",                       13),
  ("nof_events",                      1576702),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        3.697),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTGJets"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "ttH_hbb"),
  ("process_name_specific",           "ttHJetTobb_M125"),
  ("nof_files",                       25),
  ("nof_events",                      2910427),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.2934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/ttHJetTobb_M125"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ttHJetToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8_mWCutfix/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "ttHJetToNonbb_M125_amcatnlo"),
  ("nof_files",                       26),
  ("nof_events",                      2970051),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.2151),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/ttHJetToNonbb_M125_amcatnlo"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "ttHToNonbb_M125_powheg"),
  ("nof_files",                       10),
  ("nof_events",                      3819499),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.2151),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/ttHToNonbb_M125_powheg"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "TTJets_DiLept_ext1"),
  ("nof_files",                       61),
  ("nof_events",                      24115056),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        87.3),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTJets_DiLept_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "TTJets_DiLept"),
  ("nof_files",                       16),
  ("nof_events",                      6094007),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        87.3),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTJets_DiLept"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "TTJets_SingleLeptFromTbar_ext1"),
  ("nof_files",                       122),
  ("nof_events",                      48270819),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        182.18),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTJets_SingleLeptFromTbar_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "TTJets_SingleLeptFromTbar"),
  ("nof_files",                       31),
  ("nof_events",                      11925121),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        182.18),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTJets_SingleLeptFromTbar"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "TTJets_SingleLeptFromT_ext1"),
  ("nof_files",                       126),
  ("nof_events",                      49609824),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        182.18),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTJets_SingleLeptFromT_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "TTJets_SingleLeptFromT"),
  ("nof_files",                       30),
  ("nof_events",                      11859041),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        182.18),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTJets_SingleLeptFromT"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "TTTT"),
  ("nof_files",                       1),
  ("nof_events",                      104771),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.009103),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTTT"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v3/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TTW"),
  ("process_name_specific",           "TTWJetsToLNu_ext1"),
  ("nof_files",                       6),
  ("nof_events",                      1097374),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.2043),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTWJetsToLNu_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TTW"),
  ("process_name_specific",           "TTWJetsToLNu_ext2"),
  ("nof_files",                       8),
  ("nof_events",                      1603842),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.2043),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTWJetsToLNu_ext2"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TTZ"),
  ("process_name_specific",           "TTZToLL_M-1to10"),
  ("nof_files",                       1),
  ("nof_events",                      246798),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.0493),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTZToLL_M-1to10"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TTZ"),
  ("process_name_specific",           "TTZToLL_M10_ext1"),
  ("nof_files",                       5),
  ("nof_events",                      909089),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.273132),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTZToLL_M10_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TTZ"),
  ("process_name_specific",           "TTZToLL_M10_ext2"),
  ("nof_files",                       16),
  ("nof_events",                      2777061),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.273132),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTZToLL_M10_ext2"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/tZq_ll_4f_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "tZq_ll_4f"),
  ("nof_files",                       37),
  ("nof_events",                      3806636),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.0758),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/tZq_ll_4f"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "WGToLNuG_ext1"),
  ("nof_files",                       13),
  ("nof_events",                      3132470),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        585.8),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/WGToLNuG_ext1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "WGToLNuG_ext2"),
  ("nof_files",                       26),
  ("nof_events",                      6519420),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        585.8),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/WGToLNuG_ext2"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu"),
  ("nof_files",                       61),
  ("nof_events",                      16484092),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        61526.7),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/WJetsToLNu"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "WpWpJJ_EWK-QCD"),
  ("nof_files",                       1),
  ("nof_events",                      149601),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.03711),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/WpWpJJ_EWK-QCD"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/WWTo2L2Nu_13TeV-powheg/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WWTo2L2Nu"),
  ("nof_files",                       6),
  ("nof_events",                      1999193),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        10.481),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/WWTo2L2Nu"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "WWTo2L2Nu_DoubleScattering"),
  ("nof_files",                       3),
  ("nof_events",                      999361),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.1729),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/WWTo2L2Nu_DoubleScattering"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "WWW_4F"),
  ("nof_files",                       1),
  ("nof_events",                      210465),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.2086),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/WWW_4F"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "WWZ"),
  ("nof_files",                       1),
  ("nof_events",                      221511),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.1651),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/WWZ"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WZTo3LNu"),
  ("nof_files",                       5),
  ("nof_events",                      1993307),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        4.42965),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/WZTo3LNu"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "WZZ"),
  ("nof_files",                       1),
  ("nof_events",                      216296),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.05565),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/WZZ"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "ZGTo2LG"),
  ("nof_files",                       34),
  ("nof_events",                      9243007),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        131.3),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/ZGTo2LG"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "ZZTo4L"),
  ("nof_files",                       17),
  ("nof_events",                      6611207),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        1.256),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/ZZTo4L"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "ZZZ"),
  ("nof_files",                       1),
  ("nof_events",                      213100),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.01398),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/ZZZ"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/THQ_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "tH"),
  ("process_name_specific",           "THQ"),
  ("nof_files",                       5),
  ("nof_events",                      3476259),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.0325973018765),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/THQ"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/THW_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "tH"),
  ("process_name_specific",           "THW"),
  ("nof_files",                       2),
  ("nof_events",                      1499036),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.0570505487598),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/THW"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ttWW_lo/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TTWW"),
  ("process_name_specific",           "TTWW"),
  ("nof_files",                       1),
  ("nof_events",                      9994),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        0.0023023),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTWW"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/matze-faster_v8_ttH_maod_p1_3a2fa29ab1d54ae0995b28f27b405be9-v1/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "ttHToNonbb_fastsim_p1"),
  ("nof_files",                       9),
  ("nof_events",                      3291814),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          False),
  ("xsection",                        0.2151),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/ttHToNonbb_fastsim_p1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/matze-faster_v8_ttH_maod_p2_3a2fa29ab1d54ae0995b28f27b405be9-v1/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "ttHToNonbb_fastsim_p2"),
  ("nof_files",                       17),
  ("nof_events",                      6582786),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          False),
  ("xsection",                        0.2151),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/ttHToNonbb_fastsim_p2"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/matze-faster_v8_ttH_maod_p3_3a2fa29ab1d54ae0995b28f27b405be9-v1/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "ttHToNonbb_fastsim_p3"),
  ("nof_files",                       17),
  ("nof_events",                      6584779),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          False),
  ("xsection",                        0.2151),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/ttHToNonbb_fastsim_p3"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/matze-faster_v8_ttjets_dl_maod_p1_3a2fa29ab1d54ae0995b28f27b405be9-v1/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "TTTo2L2Nu_fastsim_p1"),
  ("nof_files",                       46),
  ("nof_events",                      18094332),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          False),
  ("xsection",                        87.3),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTTo2L2Nu_fastsim_p1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/matze-faster_v8_ttjets_dl_maod_p2_3a2fa29ab1d54ae0995b28f27b405be9-v1/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "TTTo2L2Nu_fastsim_p2"),
  ("nof_files",                       92),
  ("nof_events",                      36233902),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          False),
  ("xsection",                        87.3),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTTo2L2Nu_fastsim_p2"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/matze-faster_v8_ttjets_dl_maod_p3_3a2fa29ab1d54ae0995b28f27b405be9-v1/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "TTTo2L2Nu_fastsim_p3"),
  ("nof_files",                       92),
  ("nof_events",                      36199793),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          False),
  ("xsection",                        87.3),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTTo2L2Nu_fastsim_p3"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/matze-faster_v8_ttjets_sl_maod_p1_3a2fa29ab1d54ae0995b28f27b405be9-v1/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "TTToSemilepton_fastsim_p1"),
  ("nof_files",                       43),
  ("nof_events",                      17052142),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          False),
  ("xsection",                        245),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTToSemilepton_fastsim_p1"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/matze-faster_v8_ttjets_sl_maod_p2_3a2fa29ab1d54ae0995b28f27b405be9-v1/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "TTToSemilepton_fastsim_p2"),
  ("nof_files",                       86),
  ("nof_events",                      34124021),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          False),
  ("xsection",                        245),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTToSemilepton_fastsim_p2"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/matze-faster_v8_ttjets_sl_maod_p3_3a2fa29ab1d54ae0995b28f27b405be9-v1/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "TTToSemilepton_fastsim_p3"),
  ("nof_files",                       86),
  ("nof_events",                      34135498),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          False),
  ("xsection",                        245),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTToSemilepton_fastsim_p3"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/matze-faster_v9_ttW_maod_54aa74f75231422e9f4d3766cb92a64a-v1/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TTW"),
  ("process_name_specific",           "TTWJetsToLNu_fastsim"),
  ("nof_files",                       36),
  ("nof_events",                      7158309),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          False),
  ("xsection",                        0.2043),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTWJetsToLNu_fastsim"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/matze-faster_v9_ttZ_maod_54aa74f75231422e9f4d3766cb92a64a-v1/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TTZ"),
  ("process_name_specific",           "TTZToLLNuNu_fastsim"),
  ("nof_files",                       49),
  ("nof_events",                      8826709),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          False),
  ("xsection",                        0.2529),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/TTZToLLNuNu_fastsim"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2016["/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/matze-faster_v9_WZ_maod_54aa74f75231422e9f4d3766cb92a64a-v1/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WZTo3LNu_fastsim"),
  ("nof_files",                       47),
  ("nof_events",                      18814815),
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          False),
  ("xsection",                        4.102),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2017Sep20_wPreselection/ntuples/WZTo3LNu_fastsim"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

