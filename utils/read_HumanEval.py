from typing import Iterable, Dict
import gzip
import json
import os
import pandas as pd
import numpy as np

ROOT = os.getcwd()
HUMAN_EVAL = os.path.join(ROOT, "HumanEval.jsonl.gz")


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


def read_problems(evalset_file: str = HUMAN_EVAL) -> Iterable[Dict[str, Dict]]:
    return {task["task_id"]: task for task in stream_jsonl(evalset_file)}


data = read_problems(HUMAN_EVAL)
# code= data['HumanEval/0']['prompt']+data['HumanEval/0']['canonical_solution']
# test=data['HumanEval/0']['test']


code_list = []
test_list = []
for i in range(0, len(data)):
    ds = open("HumanEval/" + str(i) + ".py", "w")
    code_list.append(
        data["HumanEval/" + str(i)]["prompt"]
        + data["HumanEval/" + str(i)]["canonical_solution"]
    )
    test_list.append(data["HumanEval/" + str(i)]["test"])

    ds.write(
        data["HumanEval/" + str(i)]["prompt"]
        + data["HumanEval/" + str(i)]["canonical_solution"]
    )
    ds.write(data["HumanEval/" + str(i)]["test"])

    ds.close()
