import pandas as pd
from ast import literal_eval
import os
from generate_test_oracle import call_LLMs
import sys

def mutatePromptGenerator(function_to_test, mutant):
    mutate_prompt = f""" Generate test cases for
```python
{function_to_test}
```
The pervious test case cannot detect the change in the following code snippet.
```python
{mutant}
```
Generate a new test case to test the fault in pervious code.
```python
# test case
def test():
    assert
    """

    return mutate_prompt


def fewshotMutantPromptGenerator(fewshot_content,function_to_test,mutant):
    fewshot_mutant_prompt = f"""
{fewshot_content}

{function_to_test}
```
The pervious test case cannot detect the change in the following code snippet.
```python
{mutant}
```
Generate a new test case to test he fault in pervious code.
```python

#<test>

def test():
    assert 
"""
    return fewshot_mutant_prompt


def read_csv(csv_path):
    #read csv file with pandas
    df = pd.read_csv(csv_path)
    return df


def prompt_augmentation (prmpt, DATASET,num, input_string, output_string, mut_report_name):
    SCRIPT= str(num)
    if DATASET == "HumanEval":
        CODE_DIR_HE = os.path.join(
                os.getcwd(),
                DATASET,
                "Testing_" + DATASET, 
                "",
        )
        script_name = input_string + SCRIPT + ".py"
        input_path = os.path.join(CODE_DIR_HE , SCRIPT, "Codex", script_name)
        mut_dt = read_csv(os.path.join(CODE_DIR_HE,  mut_report_name))
        
    elif DATASET == "Refactory":
        CODE_DIR_RF = os.path.join(
                os.getcwd(),
                DATASET,
                "Reference_Scripts", "Tests", 
                "",
                )
        SCRIPT_num = "q"+str(num)
        script_name = input_string + SCRIPT_num + ".py"
        input_path = os.path.join(CODE_DIR_RF , SCRIPT_num, "Codex", script_name)
        mut_dt = read_csv(os.path.join(CODE_DIR_RF,  mut_report_name))
   

    
    mut_dt['lst_survived'] = mut_dt['lst_survived'].apply(lambda x: literal_eval(x) if "[" in x else x)

   
    PUT_inx=-200
    PUT_inx = mut_dt.index[mut_dt['name'] == script_name]

   
    if PUT_inx>=0:
        row = mut_dt.iloc[PUT_inx]
        print(row)
        if row['MS'] <1 and row['is_problematic'] != 2:

            with open(input_path) as input:
                function_to_test = input.read()

            lst_mut= row['lst_survived']
            j=0
            for mut in row['lst_survived']:
                if DATASET == "HumanEval":
                    mutant_path = os.path.join(CODE_DIR_HE, SCRIPT, "Mutants", mut)

                elif DATASET == "Refactory":
                     mutant_path = os.path.join(CODE_DIR_RF, SCRIPT_num, "Mutants", mut)

                with open(mutant_path) as input:
                    mutant_content = input.read()

                
                if prmpt =="normal":
                     mutant_prompt = mutatePromptGenerator(function_to_test, mutant_content)

                elif prmpt =="fewshot":
                    fewshot_path = os.path.join(CODE_DIR_HE, "few_shot_query.py")
                    if fewshot_path:
                        with open(fewshot_path) as fewshot:
                            fewshot_content = fewshot.read()
                    mutant_prompt = fewshotMutantPromptGenerator(fewshot_content, function_to_test, mutant_content)

                model_output = call_LLMs(mutant_prompt, "```", 200) 
                print("inside function")
                print(model_output)
                print("############")


                output= function_to_test.split("def test():")
                code= output[0]
                test = output[1]
                file_content = code + "\ndef test():\n    " + model_output
                print(file_content)
                if DATASET == "HumanEval":
                    OUTPUT_NAME =  output_string + SCRIPT + "_" + str(j) + ".py"
                    output_path = os.path.join(CODE_DIR_HE, SCRIPT, "Codex", OUTPUT_NAME)
                elif DATASET == "Refactory":
                    OUTPUT_NAME =  output_string + SCRIPT_num + "_" + str(j) + ".py"
                    output_path = os.path.join(CODE_DIR_RF, SCRIPT_num, "Codex", OUTPUT_NAME)

                j +=1
                with open(output_path, "w") as output:
                    output.write(file_content)
                output.close()

def main():
    arguments = sys.argv
    if len(arguments) != 7:
        raise SystemExit('7 inputs are required: augmented_prompt.py [prompt type] [dataset] [task_num] [input prefix name] [output prefix name] [csv report filename (.csv)]')
    else:
        prompt_type = arguments[1]
        DATASET= arguments[2]
        task_num = arguments[3]
        input_string = arguments[4]
        output_string = arguments[5]
        mut_report_name = arguments[6]
        
        if os.path.splitext(mut_report_name)[1] == ".csv":
            prompt_augmentation (prompt_type, DATASET,task_num, input_string, output_string, mut_report_name)


if __name__ == '__main__':
    main()