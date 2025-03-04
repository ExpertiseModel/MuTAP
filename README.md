![Python Version](https://img.shields.io/badge/python-3.8%20|%203.9%20|%203.10-blue)
[![DOI](https://zenodo.org/badge/DOI/10.1234/zenodo.123456.svg)](https://doi.org/10.1016/j.infsof.2024.107468)
![LLMs: Llama-2 ](https://img.shields.io/badge/LLM-Llama--2-green?logo=meta)
![LLM: Codex](https://img.shields.io/badge/LLM-GPT--4-blue?logo=openai)
![Stars](https://img.shields.io/github/stars/ExpertiseModel/MuTAP?style=social)
# MuTAP

`MuTAP` is a prompt-based learning technique to generate effective test cases with Large Language Models (LLMs). This is an implementation of a method described in <a href="https://arxiv.org/abs/2308.16557"><strong>Effective Test Generation Using Pre-trained Large Language Models and Mutation Testing</strong></a>. <br />

![](https://github.com/ExpertiseModel/MuTAP/blob/master/MuTAP_diagram.png)

`MuTAP` starts by calling an initial prompt on LLM (Codex and llama-2-chat) to generate test cases for a Program Under Test (PUT). The initial prompt uses zero-shot or few-shot learning techniques. Then, `MuTAP` attempts to repair the syntax and functional errors within the test cases generated by Codex. After generating the test cases, `MuTAP` attempts to identify and repair any syntax or functional errors. Once these issues are fixed, `MuTAP` generates different mutants for the PUT and calculates the Mutation Score (MS) of the test cases. If there are any surviving mutants, `MuTAP` uses them to augment the initial prompt and re-prompt Codex to improve its own output by generating a new test case that can kill the surviving mutants.<br />


## 1. Initial prompt on LLMC (Codex and Llama-2-chat) and syntax Fixer
At the end of this step, a unit test, including several test cases, will be generated for a `PUT`. The test cases are syntactically fixed.
```
$ python generate_test_oracle.py [prompt type] [dataset] [task_num] [script name] [output prefix name] [csv report filename (.csv)]
```
- `[prompt type]` defines the type of initial prompt. It is `normal` to indicate `zero-shot learning` or `fewshot` to indicate `few-shot learning`.
- `[dataset]` indicates the database. We have two datasets in our experiment. The first one is `HumanEval` and the second one is `Refactory` which is a benchmark for bug repairing.
- `[task_num]` is the identifier or task number within the dataset. It is within `[1,163]` for the `HumanEval` dataset, and within `[1,5]` for `Refactory`.
- `[script name]` is the name of PUT.
- `[output prefix name]` is the prefix to name the output or the test cases.
- `[csv report filename (.csv)]` is a report on different numbers of attempts on LLMC and fixing its syntax errors. It is up to 10 attempts. 

## 2. Functional repair
`semantic_err_correction.py` repairs the functional errors in assertions.
```
$ python semantic_err_correction.py [dataset] [task_num] [test name] [output prefix name] [csv report filename (.csv)]
```
- `[dataset]` indicates the database. We have two datasets in our experiment. The first one is `HumanEval` and the second one is `Refactory` which is a benchmark for bug repairing.
- `[task_num]` is the identifier or task number within the dataset. It is within `[1,163]` for the `HumanEval` dataset, and within `[1,5]` for `Refoctory`.
- `[test name]` is the name of the Initial Unit Test (IUT), generated in step 1.
- `[output prefix name]` is the prefix to name the output or the test cases.
- `[csv report filename (.csv)]` is a report on a summary of functional repair (number of assertions with functional issue, number of fixed, etc.) 

## 3. Generate mutants
We use `MutPy` [cite] to generate mutants of a `PUT`.
```
$ python Mutants_generation.py [dataset] [task_num] [script name] [csv report filename (.csv)]
```
- `[dataset]` indicates the database. We have two datasets in our experiment. The first one is `HumanEval` and the second one is `Refactory` which is a benchmark for bug repairing.
- `[task_num]` is the identifier or task number within the dataset. It is within `[1,163]` for the `HumanEval` dataset, and within `[1,5]` for `Refoctory`.
- `[script name]` is the name of PUT.
- `[csv report filename (.csv)]` generates reports on different types of mutants that it injected into `PUT`.

## 4. Calculate Mutation Score (MS)
After generating mutants, `Mutation_Score.py` calculates the MS for `IUT`.
```
$ python Mutation_Score.py [dataset] [task_num] [test name] [csv report filename (.csv)]
```
- `[dataset]` indicates the database. We have two datasets in our experiment. The first one is `HumanEval` and the second one is `Refactory` which is a benchmark for bug repairing.
- `[task_num]` is the identifier or task number within the dataset. It is within `[1,163]` for `HumanEval` dataset, and within `[1,5]` for `Refoctory`.
- `[test name]` is the name of the Initial Unit Test (IUT), generated in step 1.
- `[csv report filename (.csv)]` is a report on MS and a list of surviving mutants.

## 5. Prompt augmentation
The surviving mutant in step 4 indicates the weaknesses of `IUT'. In our prompt-based learning technique, `MuTAP` uses those mutants to improve the effectiveness of the `IUT`. The final output is named Augmented Unit Test (AUT).
```
$ python augmented_prompt.py [prompt type] [dataset] [task_num] [script name] [output prefix name] [csv report filename (.csv)]
```
- `[prompt type]` defines the type of initial prompt. It is `normal` to indicate `zero-shot learning` or `fewshot` to indicate `few-shot learning`.
- `[dataset]` indicates the database. We have two datasets in our experiment. The first one is `HumanEval` and the second one is `Refactory` which is a benchmark for bug repairing.
- `[task_num]` is the identifier or task number within the dataset. It is within `[1,163]` for the `HumanEval` dataset, and within `[1,5]` for `Refoctory`.
- `[script name]` is the name of PUT.
- `[output prefix name]` is the prefix to name the output or the test cases.
- `[csv report filename (.csv)]` is the report MS and surviving mutants, generated in step 4.

## 6. Merge test cases
This step merges `IUT` with the `AUT`.
```
python Merge_all_mut.py [dataset] [task_num] [inital test name] [augmented test name] [output name]
```
- `[dataset]` indicates the database. We have two datasets in our experiment. The first one is `HumanEval` and the second one is `Refactory` which is a benchmark for bug repairing.
- `[task_num]` is the identifier or task number within the dataset. It is within `[1,163]` for the `HumanEval` dataset, and within `[1,5]` for `Refoctory`.
- `[inital test name]` is the name of the files including initial test cases.
- `[augmented test name]` is the name of the files including test cases after calling the augmented prompt on LLMC.
- `[output name]` is the name of the file including final test cases.

## 7. Greedy minimization
This step tries to minimize the number of assertions while maximizing the MS. `greedy_test_generator.py` runs on all `PUT`
```
python greedy_test_generator.py [dataset] [csv report filename (.csv)]
```
- `[dataset]` indicates the database. We have two datasets in our experiment. The first one is `HumanEval` and the second one is `Refactory` which is a benchmark for bug repairing.
- `[csv report filename (.csv)]' is a report file on applying a greedy algorithm on all `PUT`s within the dataset.
## Example
Here is an example of `PUT` from the `HumanEval` dataset. We used the `few-shot learning` technique to generate the initial input for this example.

```python
#the PUT92
def any_int(x, y, z): 
          if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):    
               if (x+y==z) or (x+z==y) or (y+z==x):           
                    return True       
               return False   
          return False
```
```python
python generate_test_oracle.py "fewshot" "HumanEval" 92 "script_NDS_" "T_O_FS_synxfixed_" "fewshot_synx_fix.csv"
python semantic_err_correction.py "HumanEval" 92 "T_O_FS_synxfixed_" "T_O_FS_semticfixed_" "fewshot_semantic_fix.csv"
python Mutants_generation.py "HumanEval" 92 "script_NDS_" "mutant_type.csv"
python Mutation_Score.py "HumanEval" 92  "T_O_FS_semticfixed_" "fewshot_mutant_score.csv"
python augmented_prompt.py "fewshot" "HumanEval" 92 "T_O_FS_semticfixed_" "test_oracle_FS_Mut_" "fewshot_mutant_score.csv"
python Merge_all_mut.py  "HumanEval" 92 "T_O_FS_semticfixed_" "test_oracle_FS_Mut_" "T_O_FS_Mut_all_"
python greedy_test_generator.py "HumanEval" "greedy_FS_results.scv"
```

The final test case that `MuTAP` generates for this example `PUT` is as follows:
```python
def test():
    assert any_int(3, 2, 5) == True
    assert any_int(-3, -2, 1) == True
    assert any_int(3, 2, 2) == False
    assert any_int(3, 2, 1) == True
    assert any_int(3.6, -2.2, 2) == False
    
  ```
## Load Data
Test cases generated by both initial prompt types, before and after augmentation are stored into two jsonl files: `Codex_test.jsonl.gz` and `llama2_test.jsonl.gz`.
`Read_json_data.py` loads all test cases into a pickle file.


-------------------------------------------------------------------------------------------------------------------------------------------------
## Citation
<strong>Effective Test Generation Using Pre-trained Large Language Models and Mutation Testing</strong>
```
@article{,
  title={Effective Test Generation Using Pre-trained Large Language Models and Mutation Testing},
  author={Arghavan Moradi Dakhel, Amin Nikanjam, Vahid Majdinasab, Foutse Khomh, Michel C. Desmarais},
  journal={https://arxiv.org/abs/2308.16557},
  year={2023}
}
```

    
