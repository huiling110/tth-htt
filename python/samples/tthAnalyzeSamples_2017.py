from collections import OrderedDict as OD

# file generated at 2019-07-04 23:57:35 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017.py -p /hdfs/local/karl/ttHNtupleProduction/2017/2019Jul04_woPresel_nom/ntuples -N samples_2017 -E 2017 -o python/samples -g tthAnalyzeSamples_2017.py -M

samples_2017 = OD()
samples_2017["/THQ_ctcvcp_4f_Hincl_13TeV_madgraph_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "tHq"),
  ("process_name_specific",           "THQ_ctcvcp"),
  ("nof_files",                       1),
  ("nof_db_files",                    258),
  ("nof_events",                      {
    'Count'                                                      : [        51000, ],
    'CountWeighted'                                              : [        50759,        50812,        50686, ],
    'CountWeightedLHEWeightScale'                                : [        63589,        58185,        53467,        55486,        50758,        46638,        49280,        45075,        41409, ],
    'CountWeightedL1PrefireNom'                                  : [        48722,        48766,        48658, ],
    'CountWeightedL1Prefire'                                     : [        48722,        48230,        49203, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        61014,        55868,        51366,        53222,        48721,        44791,        47257,        43255,        39760, ],
    'CountWeighted_rwgt0'                                        : [       198616,       198874,       198249, ],
    'CountWeightedLHEWeightScale_rwgt0'                          : [       248150,       227554,       209472,       216641,       198612,       182807,       192482,       176436,       162377, ],
    'CountWeightedL1PrefireNom_rwgt0'                            : [       190592,       190816,       190269, ],
    'CountWeightedL1Prefire_rwgt0'                               : [       190592,       188662,       192478, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt0'              : [       238044,       218434,       201191,       207750,       190589,       175522,       184534,       169267,       155866, ],
    'CountWeighted_rwgt1'                                        : [       112089,       112224,       111898, ],
    'CountWeightedLHEWeightScale_rwgt1'                          : [       140164,       128443,       118171,       122345,       112087,       103111,       108686,        99559,        91574, ],
    'CountWeightedL1PrefireNom_rwgt1'                            : [       107578,       107694,       107408, ],
    'CountWeightedL1Prefire_rwgt1'                               : [       107578,       106491,       108639, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt1'              : [       134474,       123313,       113516,       117340,       107576,        99017,       104214,        95527,        87917, ],
    'CountWeighted_rwgt2'                                        : [        78275,        78363,        78149, ],
    'CountWeightedLHEWeightScale_rwgt2'                          : [        97950,        89708,        82494,        85486,        78274,        71971,        75934,        69518,        63913, ],
    'CountWeightedL1PrefireNom_rwgt2'                            : [        75130,        75206,        75019, ],
    'CountWeightedL1Prefire_rwgt2'                               : [        75130,        74371,        75871, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt2'              : [        93980,        86132,        79250,        81995,        75128,        69119,        72815,        66708,        61364, ],
    'CountWeighted_rwgt3'                                        : [        63730,        63798,        63633, ],
    'CountWeightedLHEWeightScale_rwgt3'                          : [        79787,        73045,        67149,        69629,        63729,        58579,        61845,        56597,        52016, ],
    'CountWeightedL1PrefireNom_rwgt3'                            : [        61171,        61230,        61086, ],
    'CountWeightedL1Prefire_rwgt3'                               : [        61171,        60554,        61774, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt3'              : [        76556,        70135,        64511,        66787,        61170,        56259,        59306,        54311,        49943, ],
    'CountWeighted_rwgt4'                                        : [        39365,        39400,        39313, ],
    'CountWeightedLHEWeightScale_rwgt4'                          : [        49353,        45129,        41446,        43059,        39364,        36147,        38238,        34952,        32092, ],
    'CountWeightedL1PrefireNom_rwgt4'                            : [        37784,        37814,        37739, ],
    'CountWeightedL1Prefire_rwgt4'                               : [        37784,        37402,        38157, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt4'              : [        47353,        43330,        39817,        41301,        37783,        34716,        36668,        33540,        30813, ],
    'CountWeighted_rwgt5'                                        : [        29545,        29567,        29511, ],
    'CountWeightedLHEWeightScale_rwgt5'                          : [        37080,        33876,        31088,        32346,        29544,        27109,        28721,        26229,        24065, ],
    'CountWeightedL1PrefireNom_rwgt5'                            : [        28355,        28374,        28327, ],
    'CountWeightedL1Prefire_rwgt5'                               : [        28355,        28068,        28636, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt5'              : [        35574,        32523,        29863,        31022,        28355,        26033,        27539,        25168,        23104, ],
    'CountWeighted_rwgt6'                                        : [        21299,        21311,        21280, ],
    'CountWeightedLHEWeightScale_rwgt6'                          : [        26771,        24426,        22392,        23348,        21298,        19522,        20729,        18906,        17327, ],
    'CountWeightedL1PrefireNom_rwgt6'                            : [        20436,        20447,        20421, ],
    'CountWeightedL1Prefire_rwgt6'                               : [        20436,        20228,        20640, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt6'              : [        25677,        23445,        21505,        22387,        20436,        18743,        19871,        18136,        16632, ],
    'CountWeighted_rwgt7'                                        : [        14630,        14635,        14623, ],
    'CountWeightedLHEWeightScale_rwgt7'                          : [        18428,        16782,        15360,        16068,        14630,        13389,        14263,        12984,        11881, ],
    'CountWeightedL1PrefireNom_rwgt7'                            : [        14030,        14034,        14025, ],
    'CountWeightedL1Prefire_rwgt7'                               : [        14030,        13885,        14172, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt7'              : [        17665,        16099,        14744,        15398,        14030,        12847,        13664,        12449,        11398, ],
    'CountWeighted_rwgt8'                                        : [         9532,         9531,         9532, ],
    'CountWeightedLHEWeightScale_rwgt8'                          : [        12042,        10936,         9986,        10497,         9531,         8702,         9316,         8458,         7721, ],
    'CountWeightedL1PrefireNom_rwgt8'                            : [         9129,         9128,         9131, ],
    'CountWeightedL1Prefire_rwgt8'                               : [         9129,         9032,         9225, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt8'              : [        11528,        10478,         9574,        10046,         9129,         8340,         8914,         8099,         7398, ],
    'CountWeighted_rwgt9'                                        : [         6010,         6006,         6015, ],
    'CountWeightedLHEWeightScale_rwgt9'                          : [         7622,         6897,         6277,         6644,         6010,         5470,         5896,         5333,         4853, ],
    'CountWeightedL1PrefireNom_rwgt9'                            : [         5741,         5737,         5746, ],
    'CountWeightedL1Prefire_rwgt9'                               : [         5741,         5675,         5804, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt9'              : [         7277,         6589,         6001,         6341,         5741,         5228,         5626,         5093,         4637, ],
    'CountWeighted_rwgt10'                                       : [         4064,         4059,         4070, ],
    'CountWeightedLHEWeightScale_rwgt10'                         : [         5165,         4660,         4230,         4505,         4064,         3689,         4000,         3608,         3274, ],
    'CountWeightedL1PrefireNom_rwgt10'                           : [         3862,         3857,         3869, ],
    'CountWeightedL1Prefire_rwgt10'                              : [         3862,         3814,         3910, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt10'             : [         4907,         4430,         4024,         4278,         3862,         3508,         3798,         3428,         3113, ],
    'CountWeighted_rwgt11'                                       : [         3692,         3690,         3696, ],
    'CountWeightedLHEWeightScale_rwgt11'                         : [         4672,         4227,         3845,         4082,         3692,         3359,         3629,         3282,         2986, ],
    'CountWeightedL1PrefireNom_rwgt11'                           : [         3493,         3490,         3498, ],
    'CountWeightedL1Prefire_rwgt11'                              : [         3493,         3446,         3540, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt11'             : [         4418,         4000,         3642,         3859,         3493,         3180,         3430,         3105,         2826, ],
    'CountWeighted_rwgt12'                                       : [         4895,         4897,         4893, ],
    'CountWeightedLHEWeightScale_rwgt12'                         : [         6141,         5596,         5122,         5373,         4895,         4480,         4782,         4356,         3987, ],
    'CountWeightedL1PrefireNom_rwgt12'                           : [         4635,         4635,         4635, ],
    'CountWeightedL1Prefire_rwgt12'                              : [         4635,         4573,         4695, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt12'             : [         5812,         5301,         4855,         5083,         4635,         4245,         4522,         4123,         3776, ],
    'CountWeighted_rwgt13'                                       : [         7673,         7682,         7662, ],
    'CountWeightedLHEWeightScale_rwgt13'                         : [         9574,         8770,         8062,         8379,         7673,         7053,         7459,         6829,         6277, ],
    'CountWeightedL1PrefireNom_rwgt13'                           : [         7286,         7292,         7278, ],
    'CountWeightedL1Prefire_rwgt13'                              : [         7286,         7195,         7376, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt13'             : [         9087,         8331,         7664,         7950,         7286,         6703,         7075,         6483,         5963, ],
    'CountWeighted_rwgt14'                                       : [        17954,        17983,        17913, ],
    'CountWeightedLHEWeightScale_rwgt14'                         : [        22329,        20526,        18928,        19536,        17953,        16554,        17386,        15975,        14728, ],
    'CountWeightedL1PrefireNom_rwgt14'                           : [        17119,        17143,        17086, ],
    'CountWeightedL1Prefire_rwgt14'                              : [        17119,        16922,        17313, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt14'             : [        21283,        19579,        18067,        18614,        17119,        15795,        16560,        15228,        14049, ],
    'CountWeighted_rwgt15'                                       : [        57412,        57512,        57274, ],
    'CountWeightedLHEWeightScale_rwgt15'                         : [        71398,        65678,        60607,        62427,        57411,        52971,        55531,        51059,        47105, ],
    'CountWeightedL1PrefireNom_rwgt15'                           : [        54905,        54989,        54786, ],
    'CountWeightedL1Prefire_rwgt15'                              : [        54905,        54311,        55489, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt15'             : [        68257,        62833,        58018,        59659,        54904,        50690,        53053,        48817,        45064, ],
    'CountWeighted_rwgt17'                                       : [       153930,       154096,       153688, ],
    'CountWeightedLHEWeightScale_rwgt17'                         : [       192679,       176422,       162203,       168152,       153927,       141503,       149357,       136702,       125654, ],
    'CountWeightedL1PrefireNom_rwgt17'                           : [       147748,       147891,       147534, ],
    'CountWeightedL1Prefire_rwgt17'                              : [       147748,       146256,       149205, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt17'             : [       184873,       169391,       155827,       161289,       147745,       135898,       143225,       131179,       120646, ],
    'CountWeighted_rwgt19'                                       : [        96739,        96829,        96609, ],
    'CountWeightedLHEWeightScale_rwgt19'                         : [       121249,       110899,       101871,       105791,        96738,        88851,        93951,        85898,        78885, ],
    'CountWeightedL1PrefireNom_rwgt19'                           : [        92855,        92932,        92742, ],
    'CountWeightedL1Prefire_rwgt19'                              : [        92855,        91916,        93772, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt19'             : [       116338,       106480,        97868,       101473,        92853,        85332,        90094,        82430,        75743, ],
    'CountWeighted_rwgt20'                                       : [        80825,        80896,        80723, ],
    'CountWeightedLHEWeightScale_rwgt20'                         : [       101366,        92665,        85084,        88434,        80824,        74203,        78530,        71762,        65876, ],
    'CountWeightedL1PrefireNom_rwgt20'                           : [        77578,        77637,        77489, ],
    'CountWeightedL1Prefire_rwgt20'                              : [        77578,        76793,        78345, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt20'             : [        97256,        88970,        81739,        84822,        77576,        71263,        75304,        68863,        63250, ],
    'CountWeighted_rwgt22'                                       : [        53723,        53758,        53670, ],
    'CountWeightedLHEWeightScale_rwgt22'                         : [        67488,        61607,        56499,        58864,        53722,        49262,        52263,        47691,        43726, ],
    'CountWeightedL1PrefireNom_rwgt22'                           : [        51553,        51583,        51509, ],
    'CountWeightedL1Prefire_rwgt22'                              : [        51553,        51028,        52066, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt22'             : [        64738,        59138,        54266,        56447,        51552,        47301,        50105,        45754,        41975, ],
    'CountWeighted_rwgt23'                                       : [        42534,        42555,        42500, ],
    'CountWeightedLHEWeightScale_rwgt23'                         : [        53495,        48783,        44699,        46652,        42533,        38968,        41415,        37753,        34585, ],
    'CountWeightedL1PrefireNom_rwgt23'                           : [        40806,        40824,        40779, ],
    'CountWeightedL1Prefire_rwgt23'                              : [        40806,        40388,        41215, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt23'             : [        51302,        46817,        42923,        44725,        40806,        37408,        39696,        36212,        33193, ],
    'CountWeighted_rwgt25'                                       : [        24880,        24882,        24875, ],
    'CountWeightedLHEWeightScale_rwgt25'                         : [        31397,        28544,        26088,        27371,        24879,        22736,        24293,        22078,        20173, ],
    'CountWeightedL1PrefireNom_rwgt25'                           : [        23842,        23843,        23841, ],
    'CountWeightedL1Prefire_rwgt25'                              : [        23842,        23590,        24088, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt25'             : [        30075,        27363,        25023,        26211,        23842,        21801,        23257,        21153,        19340, ],
    'CountWeighted_rwgt26'                                       : [        18415,        18410,        18419, ],
    'CountWeightedLHEWeightScale_rwgt26'                         : [        23292,        21130,        19275,        20303,        18415,        16796,        18018,        16340,        14902, ],
    'CountWeightedL1PrefireNom_rwgt26'                           : [        17625,        17620,        17632, ],
    'CountWeightedL1Prefire_rwgt26'                              : [        17625,        17434,        17812, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt26'             : [        22284,        20230,        18466,        19418,        17625,        16086,        17228,        15635,        14269, ],
    'CountWeighted_rwgt28'                                       : [        10210,        10200,        10222, ],
    'CountWeightedLHEWeightScale_rwgt28'                         : [        12973,        11711,        10636,        11312,        10209,         9272,        10041,         9061,         8229, ],
    'CountWeightedL1PrefireNom_rwgt28'                           : [         9721,         9711,         9736, ],
    'CountWeightedL1Prefire_rwgt28'                              : [         9721,         9603,         9836, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt28'             : [        12347,        11155,        10138,        10762,         9721,         8834,         9551,         8626,         7838, ],
    'CountWeighted_rwgt29'                                       : [         8469,         8460,         8481, ],
    'CountWeightedLHEWeightScale_rwgt29'                         : [        10758,         9707,         8811,         9389,         8469,         7687,         8339,         7522,         6827, ],
    'CountWeightedL1PrefireNom_rwgt29'                           : [         8034,         8024,         8048, ],
    'CountWeightedL1Prefire_rwgt29'                              : [         8034,         7930,         8136, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt29'             : [        10201,         9211,         8367,         8899,         8034,         7297,         7902,         7133,         6479, ],
    'CountWeighted_rwgt31'                                       : [        12697,        12706,        12685, ],
    'CountWeightedLHEWeightScale_rwgt31'                         : [        15893,        14513,        13307,        13907,        12697,        11641,        12379,        11300,        10359, ],
    'CountWeightedL1PrefireNom_rwgt31'                           : [        12033,        12038,        12027, ],
    'CountWeightedL1Prefire_rwgt31'                              : [        12033,        11877,        12187, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt31'             : [        15055,        13759,        12625,        13169,        12033,        11040,        11718,        10706,         9822, ],
    'CountWeighted_rwgt33'                                       : [       152323,       152538,       152021, ],
    'CountWeightedLHEWeightScale_rwgt33'                         : [       190118,       174476,       160715,       166017,       152320,       140289,       147530,       135338,       124632, ],
    'CountWeightedL1PrefireNom_rwgt33'                           : [       146131,       146317,       145863, ],
    'CountWeightedL1Prefire_rwgt33'                              : [       146131,       144644,       147584, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt33'             : [       182326,       167440,       154321,       159161,       146128,       134662,       141400,       129802,       119603, ],
    'CountWeighted_rwgt34'                                       : [        77571,        77675,        77423, ],
    'CountWeightedLHEWeightScale_rwgt34'                         : [        96869,        88864,        81828,        84579,        77570,        71419,        75153,        68914,        63442, ],
    'CountWeightedL1PrefireNom_rwgt34'                           : [        74429,        74519,        74299, ],
    'CountWeightedL1Prefire_rwgt34'                              : [        74429,        73675,        75167, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt34'             : [        92913,        85292,        78584,        81098,        74427,        68565,        72042,        66106,        60892, ],
    'CountWeighted_rwgt36'                                       : [        38042,        38089,        37975, ],
    'CountWeightedLHEWeightScale_rwgt36'                         : [        47547,        43588,        40115,        41507,        38041,        35006,        36876,        33792,        31092, ],
    'CountWeightedL1PrefireNom_rwgt36'                           : [        36508,        36549,        36449, ],
    'CountWeightedL1Prefire_rwgt36'                              : [        36508,        36139,        36869, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt36'             : [        45614,        41844,        38532,        39806,        36507,        33614,        35356,        32421,        29847, ],
    'CountWeighted_rwgt46'                                       : [         8642,         8657,         8622, ],
    'CountWeightedLHEWeightScale_rwgt46'                         : [        10745,         9884,         9120,         9398,         8642,         7973,         8361,         7688,         7092, ],
    'CountWeightedL1PrefireNom_rwgt46'                           : [         8256,         8268,         8239, ],
    'CountWeightedL1Prefire_rwgt46'                              : [         8256,         8165,         8346, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt46'             : [        10262,         9446,         8722,         8971,         8256,         7622,         7979,         7342,         6777, ],
    'CountWeighted_rwgt48'                                       : [        30531,        30583,        30458, ],
    'CountWeightedLHEWeightScale_rwgt48'                         : [        37987,        34937,        32236,        33205,        30530,        28166,        29529,        27147,        25042, ],
    'CountWeightedL1PrefireNom_rwgt48'                           : [        29226,        29270,        29162, ],
    'CountWeightedL1Prefire_rwgt48'                              : [        29226,        28915,        29530, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt48'             : [        36351,        33455,        30887,        31763,        29225,        26979,        28240,        25979,        23979, ],
    'CountWeighted_rwgt49'                                       : [        81763,        81899,        81573, ],
    'CountWeightedLHEWeightScale_rwgt49'                         : [       101793,        93587,        86328,        88955,        81761,        75411,        79094,        72686,        67031, ],
    'CountWeightedL1PrefireNom_rwgt49'                           : [        78326,        78442,        78159, ],
    'CountWeightedL1Prefire_rwgt49'                              : [        78326,        77506,        79128, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt49'             : [        97481,        89684,        82776,        85156,        78324,        72283,        75695,        69612,        64234, ],
  }),
  ("nof_tree_events",                 51000),
  ("nof_db_events",                   9918994),
  ("fsize_local",                     146856569), # 146.86MB, avg file size 146.86MB
  ("fsize_db",                        569542482347), # 569.54GB, avg file size 2.21GB
  ("use_it",                          True),
  ("xsection",                        0.07096),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 69),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Jul04_woPresel_nom/ntuples/THQ_ctcvcp"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/THW_ctcvcp_5f_Hincl_13TeV_madgraph_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "tHW"),
  ("process_name_specific",           "THW_ctcvcp"),
  ("nof_files",                       1),
  ("nof_db_files",                    172),
  ("nof_events",                      {
    'Count'                                                      : [        50400, ],
    'CountWeighted'                                              : [        50289,        50286,        50305, ],
    'CountWeightedLHEWeightScale'                                : [        49856,        57208,        60594,        43826,        50289,        53265,        39125,        44896,        47552, ],
    'CountWeightedL1PrefireNom'                                  : [        48440,        48429,        48456, ],
    'CountWeightedL1Prefire'                                     : [        48440,        48000,        48872, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        47967,        55104,        58418,        42165,        48440,        51352,        37643,        43245,        45844, ],
    'CountWeighted_rwgt0'                                        : [       223670,       223609,       223734, ],
    'CountWeightedLHEWeightScale_rwgt0'                          : [       221051,       254443,       270182,       194311,       223670,       237503,       173470,       199679,       212027, ],
    'CountWeightedL1PrefireNom_rwgt0'                            : [       215615,       215528,       215693, ],
    'CountWeightedL1Prefire_rwgt0'                               : [       215615,       213695,       217497, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt0'              : [       212848,       245280,       260685,       187102,       215615,       229156,       167034,       192487,       204574, ],
    'CountWeighted_rwgt1'                                        : [       120870,       120840,       120905, ],
    'CountWeightedLHEWeightScale_rwgt1'                          : [       119591,       137499,       145870,       105126,       120870,       128225,        93850,       107905,       114471, ],
    'CountWeightedL1PrefireNom_rwgt1'                            : [       116485,       116440,       116527, ],
    'CountWeightedL1Prefire_rwgt1'                               : [       116485,       115440,       117508, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt1'              : [       115121,       132510,       140703,       101196,       116485,       123683,        90343,       103990,       110417, ],
    'CountWeighted_rwgt2'                                        : [        81553,        81535,        81574, ],
    'CountWeightedLHEWeightScale_rwgt2'                          : [        80758,        92773,        98352,        70990,        81553,        86455,        63376,        72805,        77182, ],
    'CountWeightedL1PrefireNom_rwgt2'                            : [        78577,        78549,        78603, ],
    'CountWeightedL1Prefire_rwgt2'                               : [        78577,        77868,        79272, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt2'              : [        77722,        89386,        94847,        68322,        78577,        83375,        60993,        70148,        74432, ],
    'CountWeighted_rwgt3'                                        : [        64915,        64902,        64931, ],
    'CountWeightedLHEWeightScale_rwgt3'                          : [        64316,        73845,        78253,        56536,        64915,        68788,        50472,        57951,        61409, ],
    'CountWeightedL1PrefireNom_rwgt3'                            : [        62537,        62517,        62557, ],
    'CountWeightedL1Prefire_rwgt3'                               : [        62537,        61971,        63092, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt3'              : [        61889,        71141,        75455,        54403,        62537,        66328,        48568,        55829,        59214, ],
    'CountWeighted_rwgt4'                                        : [        37680,        37677,        37684, ],
    'CountWeightedLHEWeightScale_rwgt4'                          : [        37378,        42864,        45376,        32857,        37680,        39887,        29333,        33638,        35609, ],
    'CountWeightedL1PrefireNom_rwgt4'                            : [        36287,        36280,        36293, ],
    'CountWeightedL1Prefire_rwgt4'                               : [        36287,        35955,        36612, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt4'              : [        35956,        41279,        43738,        31607,        36287,        38448,        28216,        32394,        34324, ],
    'CountWeighted_rwgt5'                                        : [        27083,        27085,        27082, ],
    'CountWeightedLHEWeightScale_rwgt5'                          : [        26884,        30809,        32597,        23632,        27083,        28654,        21098,        24178,        25581, ],
    'CountWeightedL1PrefireNom_rwgt5'                            : [        26076,        26075,        26077, ],
    'CountWeightedL1Prefire_rwgt5'                               : [        26076,        25837,        26311, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt5'              : [        25855,        29664,        31414,        22727,        26076,        27614,        20290,        23279,        24653, ],
    'CountWeighted_rwgt6'                                        : [        18500,        18506,        18494, ],
    'CountWeightedLHEWeightScale_rwgt6'                          : [        18372,        21045,        22259,        16150,        18500,        19566,        14418,        16515,        17468, ],
    'CountWeightedL1PrefireNom_rwgt6'                            : [        17808,        17812,        17804, ],
    'CountWeightedL1Prefire_rwgt6'                               : [        17808,        17644,        17970, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt6'              : [        17665,        20258,        21446,        15528,        17808,        18852,        13863,        15898,        16830, ],
    'CountWeighted_rwgt7'                                        : [        11933,        11942,        11922, ],
    'CountWeightedLHEWeightScale_rwgt7'                          : [        11845,        13575,        14363,        10413,        11933,        12626,         9296,        10653,        11271, ],
    'CountWeightedL1PrefireNom_rwgt7'                            : [        11486,        11493,        11476, ],
    'CountWeightedL1Prefire_rwgt7'                               : [        11486,        11379,        11590, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt7'              : [        11388,        13066,        13837,        10010,        11486,        12164,         8937,        10254,        10859, ],
    'CountWeighted_rwgt8'                                        : [         7375,         7387,         7360, ],
    'CountWeightedLHEWeightScale_rwgt8'                          : [         7297,         8390,         8902,         6414,         7375,         7825,         5726,         6584,         6986, ],
    'CountWeightedL1PrefireNom_rwgt8'                            : [         7102,         7113,         7088, ],
    'CountWeightedL1Prefire_rwgt8'                               : [         7102,         7037,         7165, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt8'              : [         7017,         8079,         8580,         6169,         7102,         7542,         5507,         6340,         6733, ],
    'CountWeighted_rwgt9'                                        : [         4834,         4848,         4814, ],
    'CountWeightedLHEWeightScale_rwgt9'                          : [         4733,         5498,         5883,         4160,         4834,         5172,         3714,         4315,         4617, ],
    'CountWeightedL1PrefireNom_rwgt9'                            : [         4663,         4677,         4644, ],
    'CountWeightedL1Prefire_rwgt9'                               : [         4663,         4622,         4703, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt9'              : [         4560,         5304,         5681,         4008,         4663,         4994,         3578,         4163,         4458, ],
    'CountWeighted_rwgt10'                                       : [         4306,         4322,         4282, ],
    'CountWeightedLHEWeightScale_rwgt10'                         : [         4152,         4898,         5305,         3649,         4306,         4663,         3258,         3844,         4163, ],
    'CountWeightedL1PrefireNom_rwgt10'                           : [         4167,         4183,         4144, ],
    'CountWeightedL1Prefire_rwgt10'                              : [         4167,         4133,         4199, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt10'             : [         4013,         4740,         5138,         3528,         4167,         4517,         3149,         3720,         4032, ],
    'CountWeighted_rwgt11'                                       : [         5791,         5809,         5765, ],
    'CountWeightedLHEWeightScale_rwgt11'                         : [         5553,         6588,         7166,         4881,         5791,         6299,         4358,         5170,         5624, ],
    'CountWeightedL1PrefireNom_rwgt11'                           : [         5614,         5631,         5588, ],
    'CountWeightedL1Prefire_rwgt11'                              : [         5614,         5571,         5656, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt11'             : [         5377,         6386,         6952,         4727,         5614,         6111,         4220,         5011,         5456, ],
    'CountWeighted_rwgt12'                                       : [         9291,         9310,         9261, ],
    'CountWeightedLHEWeightScale_rwgt12'                         : [         8937,        10569,        11468,         7856,         9291,        10081,         7014,         8294,         8999, ],
    'CountWeightedL1PrefireNom_rwgt12'                           : [         9004,         9022,         8975, ],
    'CountWeightedL1Prefire_rwgt12'                              : [         9004,         8934,         9071, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt12'             : [         8652,        10242,        11122,         7605,         9004,         9777,         6790,         8038,         8728, ],
    'CountWeighted_rwgt13'                                       : [        14805,        14824,        14771, ],
    'CountWeightedLHEWeightScale_rwgt13'                         : [        14304,        16841,        18209,        12574,        14805,        16007,        11225,        13216,        14290, ],
    'CountWeightedL1PrefireNom_rwgt13'                           : [        14337,        14355,        14305, ],
    'CountWeightedL1Prefire_rwgt13'                              : [        14337,        14224,        14446, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt13'             : [        13838,        16309,        17648,        12164,        14337,        15514,        10859,        12799,        13849, ],
    'CountWeighted_rwgt14'                                       : [        31873,        31892,        31834, ],
    'CountWeightedLHEWeightScale_rwgt14'                         : [        30986,        36257,        39012,        27238,        31873,        34293,        24316,        28454,        30615, ],
    'CountWeightedL1PrefireNom_rwgt14'                           : [        30831,        30848,        30795, ],
    'CountWeightedL1Prefire_rwgt14'                              : [        30831,        30581,        31075, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt14'             : [        29941,        35072,        37769,        26320,        30831,        33201,        23496,        27524,        29640, ],
    'CountWeighted_rwgt15'                                       : [        90174,        90188,        90128, ],
    'CountWeightedLHEWeightScale_rwgt15'                         : [        88142,       102580,       109898,        77480,        90174,        96605,        69170,        80501,        86244, ],
    'CountWeightedL1PrefireNom_rwgt15'                           : [        87135,        87141,        87096, ],
    'CountWeightedL1Prefire_rwgt15'                              : [        87135,        86408,        87847, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt15'             : [        85078,        99123,       106287,        74787,        87135,        93431,        66766,        77788,        83410, ],
    'CountWeighted_rwgt17'                                       : [       158033,       158001,       158072, ],
    'CountWeightedLHEWeightScale_rwgt17'                         : [       156546,       179775,       190534,       137611,       158033,       167486,       122851,       141081,       149522, ],
    'CountWeightedL1PrefireNom_rwgt17'                           : [       152251,       152202,       152301, ],
    'CountWeightedL1Prefire_rwgt17'                              : [       152251,       150876,       153601, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt17'             : [       150648,       173198,       183729,       132426,       152251,       161505,       118223,       135920,       144183, ],
    'CountWeighted_rwgt19'                                       : [        93733,        93725,        93749, ],
    'CountWeightedLHEWeightScale_rwgt19'                         : [        92964,       106629,       112899,        81720,        93733,        99243,        72954,        83679,        88599, ],
    'CountWeightedL1PrefireNom_rwgt19'                           : [        90274,        90255,        90295, ],
    'CountWeightedL1Prefire_rwgt19'                              : [        90274,        89451,        91081, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt19'             : [        89431,       102694,       108831,        78614,        90274,        95668,        70181,        80591,        85407, ],
    'CountWeighted_rwgt20'                                       : [        76329,        76326,        76334, ],
    'CountWeightedLHEWeightScale_rwgt20'                         : [        75735,        86830,        91901,        66575,        76329,        80785,        59434,        68141,        72120, ],
    'CountWeightedL1PrefireNom_rwgt20'                           : [        73502,        73490,        73512, ],
    'CountWeightedL1Prefire_rwgt20'                              : [        73502,        72829,        74161, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt20'             : [        72847,        83613,        88578,        64036,        73502,        77864,        57167,        65617,        69513, ],
    'CountWeighted_rwgt22'                                       : [        47559,        47568,        47549, ],
    'CountWeightedLHEWeightScale_rwgt22'                         : [        47226,        54101,        57226,        41514,        47559,        50304,        37061,        42457,        44909, ],
    'CountWeightedL1PrefireNom_rwgt22'                           : [        45784,        45788,        45778, ],
    'CountWeightedL1Prefire_rwgt22'                              : [        45784,        45362,        46198, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt22'             : [        45411,        52082,        55141,        39918,        45784,        48471,        35637,        40873,        43272, ],
    'CountWeighted_rwgt23'                                       : [        36194,        36210,        36178, ],
    'CountWeightedLHEWeightScale_rwgt23'                         : [        35945,        41174,        43548,        31597,        36194,        38281,        28208,        32312,        34175, ],
    'CountWeightedL1PrefireNom_rwgt23'                           : [        34839,        34850,        34825, ],
    'CountWeightedL1Prefire_rwgt23'                              : [        34839,        34517,        35156, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt23'             : [        34559,        39632,        41957,        30379,        34839,        36882,        27120,        31102,        32926, ],
    'CountWeighted_rwgt25'                                       : [        19507,        19532,        19477, ],
    'CountWeightedLHEWeightScale_rwgt25'                         : [        19331,        22191,        23513,        16993,        19507,        20669,        15171,        17415,        18452, ],
    'CountWeightedL1PrefireNom_rwgt25'                           : [        18779,        18802,        18751, ],
    'CountWeightedL1Prefire_rwgt25'                              : [        18779,        18606,        18949, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt25'             : [        18588,        21363,        22657,        16339,        18779,        19916,        14587,        16765,        17780, ],
    'CountWeighted_rwgt26'                                       : [        14184,        14213,        14147, ],
    'CountWeightedLHEWeightScale_rwgt26'                         : [        13999,        16136,        17155,        12306,        14184,        15080,        10986,        12663,        13462, ],
    'CountWeightedL1PrefireNom_rwgt26'                           : [        13664,        13691,        13629, ],
    'CountWeightedL1Prefire_rwgt26'                              : [        13664,        13540,        13785, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt26'             : [        13468,        15544,        16541,        11839,        13664,        14541,        10569,        12198,        12981, ],
    'CountWeighted_rwgt28'                                       : [         9580,         9615,         9531, ],
    'CountWeightedLHEWeightScale_rwgt28'                         : [         9281,        10898,        11759,         8159,         9580,        10337,         7284,         8552,         9228, ],
    'CountWeightedL1PrefireNom_rwgt28'                           : [         9261,         9296,         9214, ],
    'CountWeightedL1Prefire_rwgt28'                              : [         9261,         9185,         9336, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt28'             : [         8962,        10535,        11379,         7878,         9261,        10003,         7033,         8268,         8930, ],
    'CountWeighted_rwgt29'                                       : [        10298,        10337,        10244, ],
    'CountWeightedLHEWeightScale_rwgt29'                         : [         9897,        11715,        12722,         8700,        10298,        11183,         7766,         9194,         9983, ],
    'CountWeightedL1PrefireNom_rwgt29'                           : [         9975,        10012,         9922, ],
    'CountWeightedL1Prefire_rwgt29'                              : [         9975,         9897,        10051, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt29'             : [         9575,        11347,        12332,         8417,         9975,        10841,         7514,         8905,         9678, ],
    'CountWeighted_rwgt31'                                       : [        24537,        24580,        24466, ],
    'CountWeightedLHEWeightScale_rwgt31'                         : [        23638,        27912,        30248,        20779,        24537,        26590,        18551,        21904,        23737, ],
    'CountWeightedL1PrefireNom_rwgt31'                           : [        23772,        23814,        23705, ],
    'CountWeightedL1Prefire_rwgt31'                              : [        23772,        23588,        23952, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt31'             : [        22878,        27042,        29330,        20111,        23772,        25782,        17954,        21222,        23017, ],
    'CountWeighted_rwgt33'                                       : [       181349,       181299,       181392, ],
    'CountWeightedLHEWeightScale_rwgt33'                         : [       178940,       206298,       219341,       157297,       181349,       192811,       140424,       161897,       172130, ],
    'CountWeightedL1PrefireNom_rwgt33'                           : [       174883,       174814,       174937, ],
    'CountWeightedL1Prefire_rwgt33'                              : [       174883,       173341,       176394, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt33'             : [       172366,       198943,       211709,       151516,       174883,       186102,       135266,       156123,       166141, ],
    'CountWeighted_rwgt34'                                       : [        89673,        89649,        89697, ],
    'CountWeightedLHEWeightScale_rwgt34'                         : [        88557,       102010,       108384,        77846,        89673,        95274,        69496,        80054,        85055, ],
    'CountWeightedL1PrefireNom_rwgt34'                           : [        86458,        86424,        86488, ],
    'CountWeightedL1Prefire_rwgt34'                              : [        86458,        85692,        87209, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt34'             : [        85286,        98353,       104592,        74971,        86458,        91941,        66929,        77184,        82080, ],
    'CountWeighted_rwgt36'                                       : [        42061,        42050,        42073, ],
    'CountWeightedLHEWeightScale_rwgt36'                         : [        41589,        47848,        50786,        36558,        42061,        44643,        32637,        37549,        39855, ],
    'CountWeightedL1PrefireNom_rwgt36'                           : [        40541,        40525,        40556, ],
    'CountWeightedL1Prefire_rwgt36'                              : [        40541,        40179,        40896, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt36'             : [        40041,        46119,        48995,        35197,        40541,        43069,        31422,        36192,        38450, ],
    'CountWeighted_rwgt46'                                       : [        14249,        14253,        14238, ],
    'CountWeightedLHEWeightScale_rwgt46'                         : [        13899,        16209,        17394,        12218,        14249,        15290,        10908,        12721,        13650, ],
    'CountWeightedL1PrefireNom_rwgt46'                           : [        13774,        13777,        13765, ],
    'CountWeightedL1Prefire_rwgt46'                              : [        13774,        13661,        13886, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt46'             : [        13422,        15669,        16829,        11798,        13774,        14793,        10533,        12297,        13207, ],
    'CountWeighted_rwgt48'                                       : [        45174,        45174,        45162, ],
    'CountWeightedLHEWeightScale_rwgt48'                         : [        44255,        51389,        54956,        38902,        45174,        48309,        34729,        40328,        43127, ],
    'CountWeightedL1PrefireNom_rwgt48'                           : [        43632,        43628,        43623, ],
    'CountWeightedL1Prefire_rwgt48'                              : [        43632,        43263,        43993, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt48'             : [        42697,        49634,        53126,        37532,        43632,        46700,        33507,        38951,        41691, ],
    'CountWeighted_rwgt49'                                       : [       114600,       114589,       114589, ],
    'CountWeightedLHEWeightScale_rwgt49'                         : [       112486,       130367,       139199,        98880,       114600,       122363,        88275,       102308,       109238, ],
    'CountWeightedL1PrefireNom_rwgt49'                           : [       110643,       110620,       110640, ],
    'CountWeightedL1Prefire_rwgt49'                              : [       110643,       109697,       111568, ],
    'CountWeightedLHEWeightScaleL1PrefireNom_rwgt49'             : [       108481,       125865,       134510,        95360,       110643,       118241,        85131,        98775,       105559, ],
  }),
  ("nof_tree_events",                 50400),
  ("nof_db_events",                   4719999),
  ("fsize_local",                     170162632), # 170.16MB, avg file size 170.16MB
  ("fsize_db",                        308444472684), # 308.44GB, avg file size 1.79GB
  ("use_it",                          True),
  ("xsection",                        0.01561),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 69),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Jul04_woPresel_nom/ntuples/THW_ctcvcp"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "ttHJetToNonbb_M125_amcatnlo"),
  ("nof_files",                       1),
  ("nof_db_files",                    208),
  ("nof_events",                      {
    'Count'                                                      : [        65452, ],
    'CountWeighted'                                              : [        22455,        22443,        22473, ],
    'CountWeightedLHEWeightScale'                                : [        22906,        23311,        23703,        22808,        22455,        22179,        21395,        20690,        20108, ],
    'CountWeightedL1PrefireNom'                                  : [        21660,        21648,        21670, ],
    'CountWeightedL1Prefire'                                     : [        21660,        21467,        21848, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        22052,        22464,        22862,        21981,        21659,        21409,        20633,        19969,        19421, ],
  }),
  ("nof_tree_events",                 65452),
  ("nof_db_events",                   9779592),
  ("fsize_local",                     211999808), # 212.00MB, avg file size 212.00MB
  ("fsize_db",                        625507074411), # 625.51GB, avg file size 3.01GB
  ("use_it",                          True),
  ("xsection",                        0.2118),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Jul04_woPresel_nonNom_sync/ntuples/ttHJetToNonbb_M125_amcatnlo"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/ttHJet_ctcvcp/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ctcvcp"),
  ("process_name_specific",           "ttH_ctcvcp"),
  ("nof_files",                       1),
  ("nof_db_files",                    208),
  ("nof_events",                      {
    'Count'                                                      : [        65452, ],
    'CountWeighted'                                              : [        22455,        22443,        22473, ],
    'CountWeightedLHEWeightScale'                                : [        22906,        23311,        23703,        22808,        22455,        22179,        21395,        20690,        20108, ],
    'CountWeightedL1PrefireNom'                                  : [        21660,        21648,        21670, ],
    'CountWeightedL1Prefire'                                     : [        21660,        21467,        21848, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        22052,        22464,        22862,        21981,        21659,        21409,        20633,        19969,        19421, ],
  }),
  ("nof_tree_events",                 65452),
  ("nof_db_events",                   9779592),
  ("fsize_local",                     211999808), # 212.00MB, avg file size 212.00MB
  ("fsize_db",                        625507074411), # 625.51GB, avg file size 3.01GB
  ("use_it",                          True),
  ("xsection",                        0.2118),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Jul04_woPresel_nonNom_sync/ntuples/ttHJetToNonbb_M125_amcatnlo"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/ttZJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TTZ"),
  ("process_name_specific",           "TTZToLL_M10"),
  ("nof_files",                       1),
  ("nof_db_files",                    208),
  ("nof_events",                      {
    'Count'                                                      : [        65452, ],
    'CountWeighted'                                              : [        22455,        22443,        22473, ],
    'CountWeightedLHEWeightScale'                                : [        22906,        23311,        23703,        22808,        22455,        22179,        21395,        20690,        20108, ],
    'CountWeightedL1PrefireNom'                                  : [        21660,        21648,        21670, ],
    'CountWeightedL1Prefire'                                     : [        21660,        21467,        21848, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        22052,        22464,        22862,        21981,        21659,        21409,        20633,        19969,        19421, ],
  }),
  ("nof_tree_events",                 65452),
  ("nof_db_events",                   9779592),
  ("fsize_local",                     211999808), # 212.00MB, avg file size 212.00MB
  ("fsize_db",                        625507074411), # 625.51GB, avg file size 3.01GB
  ("use_it",                          True),
  ("xsection",                        0.2118),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Jul04_woPresel_nonNom_sync/ntuples/ttHJetToNonbb_M125_amcatnlo"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/ttWJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TTW"),
  ("process_name_specific",           "TTW"),
  ("nof_files",                       1),
  ("nof_db_files",                    208),
  ("nof_events",                      {
    'Count'                                                      : [        65452, ],
    'CountWeighted'                                              : [        22455,        22443,        22473, ],
    'CountWeightedLHEWeightScale'                                : [        22906,        23311,        23703,        22808,        22455,        22179,        21395,        20690,        20108, ],
    'CountWeightedL1PrefireNom'                                  : [        21660,        21648,        21670, ],
    'CountWeightedL1Prefire'                                     : [        21660,        21467,        21848, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        22052,        22464,        22862,        21981,        21659,        21409,        20633,        19969,        19421, ],
  }),
  ("nof_tree_events",                 65452),
  ("nof_db_events",                   9779592),
  ("fsize_local",                     211999808), # 212.00MB, avg file size 212.00MB
  ("fsize_db",                        625507074411), # 625.51GB, avg file size 3.01GB
  ("use_it",                          True),
  ("xsection",                        0.2118),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Jul04_woPresel_nonNom_sync/ntuples/ttHJetToNonbb_M125_amcatnlo"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/ttWWJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TTWW"),
  ("process_name_specific",           "TTWW"),
  ("nof_files",                       1),
  ("nof_db_files",                    208),
  ("nof_events",                      {
    'Count'                                                      : [        65452, ],
    'CountWeighted'                                              : [        22455,        22443,        22473, ],
    'CountWeightedLHEWeightScale'                                : [        22906,        23311,        23703,        22808,        22455,        22179,        21395,        20690,        20108, ],
    'CountWeightedL1PrefireNom'                                  : [        21660,        21648,        21670, ],
    'CountWeightedL1Prefire'                                     : [        21660,        21467,        21848, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        22052,        22464,        22862,        21981,        21659,        21409,        20633,        19969,        19421, ],
  }),
  ("nof_tree_events",                 65452),
  ("nof_db_events",                   9779592),
  ("fsize_local",                     211999808), # 212.00MB, avg file size 212.00MB
  ("fsize_db",                        625507074411), # 625.51GB, avg file size 3.01GB
  ("use_it",                          True),
  ("xsection",                        0.2118),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Jul04_woPresel_nonNom_sync/ntuples/ttHJetToNonbb_M125_amcatnlo"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/ttJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "TT"),
  ("process_name_specific",           "TT"),
  ("nof_files",                       1),
  ("nof_db_files",                    208),
  ("nof_events",                      {
    'Count'                                                      : [        65452, ],
    'CountWeighted'                                              : [        22455,        22443,        22473, ],
    'CountWeightedLHEWeightScale'                                : [        22906,        23311,        23703,        22808,        22455,        22179,        21395,        20690,        20108, ],
    'CountWeightedL1PrefireNom'                                  : [        21660,        21648,        21670, ],
    'CountWeightedL1Prefire'                                     : [        21660,        21467,        21848, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        22052,        22464,        22862,        21981,        21659,        21409,        20633,        19969,        19421, ],
  }),
  ("nof_tree_events",                 65452),
  ("nof_db_events",                   9779592),
  ("fsize_local",                     211999808), # 212.00MB, avg file size 212.00MB
  ("fsize_db",                        625507074411), # 625.51GB, avg file size 3.01GB
  ("use_it",                          True),
  ("xsection",                        0.2118),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Jul04_woPresel_nonNom_sync/ntuples/ttHJetToNonbb_M125_amcatnlo"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/VHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "VH"),
  ("process_name_specific",           "VH"),
  ("nof_files",                       1),
  ("nof_db_files",                    208),
  ("nof_events",                      {
    'Count'                                                      : [        65452, ],
    'CountWeighted'                                              : [        22455,        22443,        22473, ],
    'CountWeightedLHEWeightScale'                                : [        22906,        23311,        23703,        22808,        22455,        22179,        21395,        20690,        20108, ],
    'CountWeightedL1PrefireNom'                                  : [        21660,        21648,        21670, ],
    'CountWeightedL1Prefire'                                     : [        21660,        21467,        21848, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        22052,        22464,        22862,        21981,        21659,        21409,        20633,        19969,        19421, ],
  }),
  ("nof_tree_events",                 65452),
  ("nof_db_events",                   9779592),
  ("fsize_local",                     211999808), # 212.00MB, avg file size 212.00MB
  ("fsize_db",                        625507074411), # 625.51GB, avg file size 3.01GB
  ("use_it",                          True),
  ("xsection",                        0.2118),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Jul04_woPresel_nonNom_sync/ntuples/ttHJetToNonbb_M125_amcatnlo"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/EWKJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "EWK"),
  ("nof_files",                       1),
  ("nof_db_files",                    208),
  ("nof_events",                      {
    'Count'                                                      : [        65452, ],
    'CountWeighted'                                              : [        22455,        22443,        22473, ],
    'CountWeightedLHEWeightScale'                                : [        22906,        23311,        23703,        22808,        22455,        22179,        21395,        20690,        20108, ],
    'CountWeightedL1PrefireNom'                                  : [        21660,        21648,        21670, ],
    'CountWeightedL1Prefire'                                     : [        21660,        21467,        21848, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        22052,        22464,        22862,        21981,        21659,        21409,        20633,        19969,        19421, ],
  }),
  ("nof_tree_events",                 65452),
  ("nof_db_events",                   9779592),
  ("fsize_local",                     211999808), # 212.00MB, avg file size 212.00MB
  ("fsize_db",                        625507074411), # 625.51GB, avg file size 3.01GB
  ("use_it",                          True),
  ("xsection",                        0.2118),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Jul04_woPresel_nonNom_sync/ntuples/ttHJetToNonbb_M125_amcatnlo"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["/RaresJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "Rares"),
  ("process_name_specific",           "Rares"),
  ("nof_files",                       1),
  ("nof_db_files",                    208),
  ("nof_events",                      {
    'Count'                                                      : [        65452, ],
    'CountWeighted'                                              : [        22455,        22443,        22473, ],
    'CountWeightedLHEWeightScale'                                : [        22906,        23311,        23703,        22808,        22455,        22179,        21395,        20690,        20108, ],
    'CountWeightedL1PrefireNom'                                  : [        21660,        21648,        21670, ],
    'CountWeightedL1Prefire'                                     : [        21660,        21467,        21848, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        22052,        22464,        22862,        21981,        21659,        21409,        20633,        19969,        19421, ],
  }),
  ("nof_tree_events",                 65452),
  ("nof_db_events",                   9779592),
  ("fsize_local",                     211999808), # 212.00MB, avg file size 212.00MB
  ("fsize_db",                        625507074411), # 625.51GB, avg file size 3.01GB
  ("use_it",                          True),
  ("xsection",                        0.2118),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Jul04_woPresel_nonNom_sync/ntuples/ttHJetToNonbb_M125_amcatnlo"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])

samples_2017["sum_events"] = [
  [ 'ST_s-channel_4f_leptonDecays',                    'ST_s-channel_4f_leptonDecays_PSweights',           ],
  [ 'DYJetsToLL_M-4to50_HT-200to400',                  'DYJetsToLL_M-4to50_HT-200to400_ext1',              ],
  [ 'DYJetsToLL_M50_HT100to200',                       'DYJetsToLL_M50_HT100to200_ext1',                   ],
  [ 'TTTT',                                            'TTTT_PSweights',                                   ],
  [ 'DY3JetsToLL_M-50',                                'DY3JetsToLL_M-50_ext1',                            ],
  [ 'ST_t-channel_top_4f_inclusiveDecays',             'ST_t-channel_top_4f_inclusiveDecays_PSweights',    ],
  [ 'DYJetsToLL_M-4to50_HT-400to600',                  'DYJetsToLL_M-4to50_HT-400to600_ext1',              ],
  [ 'WWToLNuQQ',                                       'WWToLNuQQ_ext1',                                  'WWToLNuQQ_PSweights_ext1',                         ],
  [ 'TTWJetsToLNu',                                    'TTWJetsToLNu_PSweights',                           ],
  [ 'TTToHadronic',                                    'TTToHadronic_PSweights',                           ],
  [ 'TTTo2L2Nu',                                       'TTTo2L2Nu_PSweights',                              ],
  [ 'DYJetsToLL_M-10to50',                             'DYJetsToLL_M-10to50_ext1',                         ],
  [ 'ST_t-channel_antitop_4f_inclusiveDecays',         'ST_t-channel_antitop_4f_inclusiveDecays_PSweights',  ],
  [ 'DY1JetsToLL_M-50_ext1',                           'DY1JetsToLL_M-50',                                 ],
  [ 'WWTo2L2Nu',                                       'WWTo2L2Nu_PSweights_ext1',                         ],
  [ 'DYJetsToLL_M50_HT200to400',                       'DYJetsToLL_M50_HT200to400_ext1',                   ],
  [ 'DYJetsToLL_M-4to50_HT-600toInf',                  'DYJetsToLL_M-4to50_HT-600toInf_ext1',              ],
  [ 'WWTo4Q',                                          'WWTo4Q_PSweights_ext1',                            ],
  [ 'DY2JetsToLL_M-50',                                'DY2JetsToLL_M-50_ext1',                            ],
  [ 'TTZToLL_M10',                                     'TTZToLL_M10_PSweights',                            ],
  [ 'TTGJets',                                         'TTGJets_ext1',                                     ],
  [ 'ST_tW_top_5f_inclusiveDecays',                    'ST_tW_top_5f_inclusiveDecays_PSweights',           ],
  [ 'ZZTo4L',                                          'ZZTo4L_ext1',                                     'ZZTo4L_ext2',                                      ],
  [ 'WJetsToLNu_madgraphMLM',                          'WJetsToLNu_madgraphMLM_ext1',                      ],
  [ 'TTToSemiLeptonic',                                'TTToSemiLeptonic_PSweights',                       ],
  [ 'TTWJets_LO',                                      'TTWJets_LO_ext1',                                  ],
  [ 'TTZJets_LO',                                      'TTZJets_LO_ext1',                                  ],
  [ 'ttHToNonbb_M125_powheg',                          'ttHToNonbb_M125_powheg_ext1',                      ],
  [ 'DYBBJetsToLL_M-50',                               'DYBBJetsToLL_M-50_ext1',                           ],
  [ 'ST_tW_antitop_5f_inclusiveDecays',                'ST_tW_antitop_5f_inclusiveDecays_PSweights',       ],
  [ 'GluGluHToTauTau',                                 'GluGluHToTauTau_ext1',                             ],
  [ 'DYJetsToLL_M50_HT400to600',                       'DYJetsToLL_M50_HT400to600_ext1',                   ],
  [ 'DYJetsToLL_M-50',                                 'DYJetsToLL_M-50_ext1',                             ],
  [ 'DYJetsToLL_M-50_amcatnloFXFX',                    'DYJetsToLL_M-50_amcatnloFXFX_ext1',                ],
  [ 'DYJetsToLL_M-4to50_HT-100to200',                  'DYJetsToLL_M-4to50_HT-100to200_ext1',              ],
]

