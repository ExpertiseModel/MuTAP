from ast import Dict
import gzip
import json
import os
import pickle
from typing import Iterable


#Based on model types, test are in Codex_test.json.gz or lama2_test.jsonl.gz
CODE_DIR = os.path.join(os.getcwd(), "llama2_test.jsonl.gz")


#stream_jsonl is from HumanEval 
def stream_jsonl(filename: str) -> Iterable[Dict]:
    """
    Parses each jsonl line and yields it as a dictionary
    """
    if filename.endswith(".gz"):
        with open(filename, "rb") as gzfp:
            with gzip.open(gzfp, "rt") as fp:
                for line in fp:
                    if any(not x.isspace() for x in line):
                        yield json.loads(line)
    else:
        with open(filename, "r") as fp:
            for line in fp:
                if any(not x.isspace() for x in line):
                    yield json.loads(line)


def read_problems(evalset_file) -> Iterable[Dict[str, Dict]]:
    return {task["task_id"]: task for task in stream_jsonl(evalset_file)}




#write data into pickle file
def Write_into_pickle(ROOT, problems):
    cache_file = os.path.join(ROOT, "test_plus.pkl")
    if os.path.exists(cache_file):
        print(f"Load tests from {cache_file}")
        with open(cache_file, "rb") as f:
            return pickle.load(f)

    print("Computing expected output...")
    
    expected_output = {}
    for task_id, problem in problems.items():
        oracle = {}
        oracle ["solution"]= problem ["solution"]
        oracle ["zero_initial_test"] = problem ["zero_initial_test"]
        oracle ["few_initial_test"] = problem ["few_initial_test"]
        oracle ["zero_augmented_test"] = problem ["zero_augmented_test"]
        oracle ["few_augmented_test"] = problem ["few_augmented_test"]

        expected_output[task_id] = oracle
       
    with open(cache_file, "wb") as f:
        pickle.dump(expected_output, f)

    return expected_output


#load data
load_data = read_problems (CODE_DIR)
data = Write_into_pickle(load_data)