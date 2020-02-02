
from tthAnalysis.HiggsToTauTau.jobTools import generate_file_ids, generate_input_list, logging

import re

def initDict(dictionary, keys):
    """Auxiliary function to initialize dictionary for access with multiple keys
    """
    dictionary_at_keylevel = dictionary
    numKeys = len(keys)
    for idxKey in range(numKeys - 1):
        key = keys[idxKey]
        if key not in dictionary_at_keylevel.keys():
            dictionary_at_keylevel[key] = {}
        dictionary_at_keylevel = dictionary_at_keylevel[key]

def append_to_key(key, part):
    new_key = key
    if len(new_key) > 0:
        new_key += "_"
    new_key += str(part)
    return new_key

def getKey(*args):
    key = ""
    for part in args:
        if part != "":
            key = append_to_key(key, part)
    return key

def create_cfg(cfg_file_original, cfg_file_modified, lines):
    """Auxiliary function to clone config file.
       The lines given as argument are added to the end of the cloned file,
       overwriting some of the configuration parameters defined in the original file.
    """
    f_original = open(cfg_file_original, "r")
    cfg_original = f_original.read()
    f_original.close()
    cfg_modified = cfg_original
    cfg_modified += "\n"
    for line in lines:
        cfg_modified += "%s\n" % line
    cfg_modified += "\n"
    f_modified = open(cfg_file_modified, "w")
    f_modified.write(cfg_modified)
    f_modified.close()

def createFile(fileName, lines, nofNewLines = 2):
    """Auxiliary function to write new config file,
       containg the lines given as argument.
    """
    content = "\n".join(lines)
    content += nofNewLines * "\n"
    with open(fileName, "w") as f:
      f.write(content)

def initializeInputFileIds(sample_info, max_files_per_job):
    """Retrieves the number of input ROOT files (Ntuples) corresponding to a given sample
       and fills the number into the dictionary 'inputFileIds', with the name of the sample as key

       TODO: add blacklist to the secondary storage as well
    """
    #print "<initializeInputFileIds>:"
    nof_inputFiles = sample_info["nof_files"]
    store_dirs = sample_info["local_paths"]
    assert(len(store_dirs) <= 2), "There is more than one secondary dir!"
    primary_store, secondary_store = "", ""
    secondary_files, blacklist = [], []
    for store_dir in store_dirs:
        if store_dir["selection"] == "*":
            primary_store = store_dir["path"]
            if "blacklist" in store_dir:
                blacklist = store_dir["blacklist"]
        else:
            secondary_store = store_dir["path"]
            secondary_files = map(lambda x: int(x), store_dir[
                "selection"].split(","))
    inputFileIds = generate_file_ids(nof_inputFiles, max_files_per_job, blacklist)
    return ( inputFileIds, secondary_files, primary_store, secondary_store )

def generateInputFileList(sample_info, max_units_per_job, by_file = True):
    if type(max_units_per_job) == int:
        max_files_per_job_int = max_units_per_job
    else:
        assert(type(max_units_per_job) == str)
        max_files_per_job_default = -1
        max_files_per_job_by_cat = {}
        max_files_per_job_by_sample = {}
        max_files_per_job_split = max_units_per_job.split(',')
        for max_files_per_job_setting in max_files_per_job_split:
            max_files_per_job_setting_split = max_files_per_job_setting.split(':')
            if len(max_files_per_job_setting_split) == 1:
                assert(max_files_per_job_default < 0)
                max_files_per_job_default = int(max_files_per_job_setting_split[0])
            elif len(max_files_per_job_setting_split) == 3:
                max_files_per_job_type = max_files_per_job_setting_split[0]
                max_files_per_job_key = max_files_per_job_setting_split[1]
                max_files_per_job_value = int(max_files_per_job_setting_split[2])
                if max_files_per_job_type == 'cat':
                    assert(max_files_per_job_key not in max_files_per_job_by_cat)
                    max_files_per_job_by_cat[max_files_per_job_key] = max_files_per_job_value
                elif max_files_per_job_type == 'name':
                    assert(max_files_per_job_key not in max_files_per_job_by_sample)
                    max_files_per_job_by_sample[max_files_per_job_key] = max_files_per_job_value
                else:
                    raise RuntimeError("Invalid key '%s' in option: %s" % (max_files_per_job_type, max_units_per_job))
            else:
                raise RuntimeError("Invalid option: %s" % max_units_per_job)
        max_files_per_job_int = max_files_per_job_default
        for cat, value in max_files_per_job_by_cat.items():
            if re.match(cat, sample_info['sample_category']):
                max_files_per_job_int = value
        for name, value in max_files_per_job_by_sample.items():
            if re.match(name, sample_info['process_name_specific']):
                max_files_per_job_int = value
    assert(max_files_per_job_int > 0)
    inputFileList = {}
    max_files_per_job = max_files_per_job_int if by_file else -1
    max_events_per_job = max_units_per_job if not by_file else -1
    if sample_info['parent'].endswith(('/MINIAOD', '/MINIAODSIM')):
        if by_file:
            inputFileList = {
                (jobIdx + 1) : filePaths for jobIdx, filePaths in enumerate(
                    list(map(
                        lambda sampleEntry: sampleEntry[0],
                        sample_info['local_paths'][fileIdx:fileIdx + max_files_per_job]
                    )) for fileIdx in range(0, len(sample_info['local_paths']), max_files_per_job)
                )
            }
        else:
            jobIdx = 1
            for fileIdx in range(0, len(sample_info['local_paths'])):
                file_name = sample_info['local_paths'][fileIdx][0]
                nof_events = sample_info['local_paths'][fileIdx][1]
                if nof_events < max_events_per_job:
                    inputFileList[jobIdx] = { 'name' : file_name, 'skip' : -1, 'max' : -1 }
                    jobIdx += 1
                else:
                    nof_splits = int(math.ceil(float(nof_events) / max_events_per_job))
                    assert(nof_splits > 1)
                    for splitIdx in range(nof_splits):
                        inputFileList[jobIdx] = {
                            'name' : file_name,
                            'skip' : splitIdx * max_events_per_job,
                            'max'  : min(max_events_per_job, nof_events - splitIdx * max_events_per_job),
                        }
                        assert(inputFileList[jobIdx]['skip'] >= 0)
                        assert(inputFileList[jobIdx]['max'] > 0)
                        jobIdx += 1
    else:
        if not by_file:
            raise RuntimeError("Post-processed Ntuples can only by distributed by files per job")
        ( inputFileIds, secondary_files, primary_store, secondary_store ) = initializeInputFileIds(sample_info, max_files_per_job)
        if max_files_per_job > 1:
            for jobId in range(len(inputFileIds)):
                inputFileList[jobId + 1] = generate_input_list(inputFileIds[jobId], secondary_files, primary_store, secondary_store)
        elif max_files_per_job == 1:
            for jobId_it in range(len(inputFileIds)):
                jobId = inputFileIds[jobId_it]
                inputFileList[jobId[0]] = generate_input_list(jobId, secondary_files, primary_store, secondary_store)
    return inputFileList

def createMakefile(makefileName, targets, lines_makefile, filesToClean = None, isSbatch = False, phoniesToAdd = []):
    """Creates Makefile that runs the complete analysis workfow.
    """

    lines_makefile_with_header = []
    lines_makefile_with_header.append(".DEFAULT_GOAL := all")
    lines_makefile_with_header.append("SHELL := /bin/bash")
    lines_makefile_with_header.append("")
    lines_makefile_with_header.append("all: %s" % " ".join(targets))
    lines_makefile_with_header.append("")
    phonies = []
    if filesToClean:
        phonies.append('clean')
    if isSbatch:
        phonies.append(' '.join(phoniesToAdd))
    if len(phonies) > 0:
        lines_makefile_with_header.append(".PHONY: %s" % ' '.join(phonies))
        lines_makefile_with_header.append("")
    if filesToClean:
        lines_makefile_with_header.append("clean:")
        for fileToClean in filesToClean:
            lines_makefile_with_header.append("\trm -f %s" % fileToClean)
        lines_makefile_with_header.append("")
    lines_makefile_with_header.extend(lines_makefile)
    createFile(makefileName, lines_makefile_with_header)

def is_dymc_reweighting(dbs_name):
  return dbs_name.startswith('/DY')       and \
         'M-50' in dbs_name               and \
         not dbs_name.startswith('/DYBB') and \
         'amcatnloFXFX' not in dbs_name

def is_dymc_normalization(dbs_name):
  return dbs_name.startswith('/DY')       and \
         'M-50' in dbs_name               and \
         'amcatnloFXFX' in dbs_name

def check_sample_pairs(samples):
    retValue = True
    for sample_name_outer, sample_info_outer in samples.items():
        if sample_name_outer == "sum_events":
            continue
        for sample_name_inner, sample_info_inner in samples.items():
            if sample_name_inner == "sum_events":
                continue
            if (sample_name_inner.startswith('/TTTo')          and sample_name_outer.startswith('/TTJets')) or \
               (sample_name_inner.startswith('/WGToLNuG_Tune') and sample_name_outer.startswith('/WGToLNuG_01J')) or \
               (sample_name_inner.startswith('/WWTo1L1Nu2Q')   and sample_name_outer.startswith('/WWToLNuQQ')) or \
               (sample_name_inner.startswith('/TTWJetsToLNu')  and sample_name_outer.startswith('/ttWJets')) or \
               (sample_name_inner.startswith('/TTZToLL')       and sample_name_outer.startswith('/ttZJets')) or \
               (sample_name_inner.startswith('/TTJets_Tune')   and sample_name_outer.startswith(('/TTJets_DiLept', '/TTJets_SingleLeptFromT'))) or \
               (sample_name_inner.startswith('/DY') and 'M-50' in sample_name_inner and 'amcatnloFXFX'     in sample_name_inner and
                sample_name_outer.startswith('/DY') and 'M-50' in sample_name_outer and 'amcatnloFXFX' not in sample_name_outer) or \
               (sample_name_inner.startswith('/WZTo3LNu')    and 'amcatnloFXFX'     in sample_name_inner and
                sample_name_outer.startswith('/WZTo3LNu')    and 'amcatnloFXFX' not in sample_name_outer) or \
               (sample_name_inner.startswith('/WZTo3LNu') and 'Jets_MLL'     in sample_name_inner and # no stitching weights, yet
                sample_name_outer.startswith('/WZTo3LNu') and 'Jets_MLL' not in sample_name_outer):
                if sample_info_outer["use_it"] and sample_info_inner["use_it"]:
                    retValue = False
                    logging.error("Samples {} and {} enabled simultaneously".format(sample_name_outer, sample_name_inner))
    return retValue

def split_stitched(samples_to_stitch, startstring):
    assert(startstring in [ 'DY', 'W' ])
    samples_inclusive = []
    samples_binned = []
    for sample_set in samples_to_stitch:
        for sample_key, sample_value in sample_set.items():
            if sample_key == 'inclusive':
                inclusive_samples = list(filter(
                    lambda sample_name: sample_name.startswith(startstring), sample_value['samples']
                ))
                samples_inclusive.extend(inclusive_samples)
            else:
                for sample_binned_value in sample_value:
                    binned_samples = list(filter(
                        lambda sample_name: sample_name.startswith(startstring), sample_binned_value['samples']
                    ))
                    samples_binned.extend(binned_samples)
    return samples_inclusive, samples_binned

def get_tH_weight_str(kt, kv, cosa = None):
    result = "kt_%.3g_kv_%.6g" % (kt, kv)
    if cosa:
        result += "_cosa_%.4g" % cosa
    result = result.replace('.', 'p').replace('-', 'm')
    return result

def get_tH_SM_str():
    return get_tH_weight_str(1.0, 1.0)

def get_tH_params(kt_kv_cosa_str):
    kt_kv_cosa_str_repl = kt_kv_cosa_str.replace('m', '-').replace('p', '.')
    cosa_idx = kt_kv_cosa_str_repl.find('cosa_')
    kt_str = kt_kv_cosa_str_repl[kt_kv_cosa_str_repl.find('kt_') + 3 : kt_kv_cosa_str_repl.find('kv_') - 1]
    kv_str = kt_kv_cosa_str_repl[kt_kv_cosa_str_repl.find('kv_') + 3 : len(kt_kv_cosa_str_repl) if cosa_idx < 0 else (cosa_idx - 1)]
    cosa_str = '' if cosa_idx < 0 else kt_kv_cosa_str_repl[cosa_idx + 5 : ]
    return (float(kt_str), float(kv_str), float(cosa_str) if cosa_str else None)
