import pandas as pd
from ast import literal_eval
import os
from generate_test_oracle import call_LLMs

def mutatePromptGenerator(function_to_test, mutant):
    mutate_prompt = f""" Generate test cases for
```python
{function_to_test}
```
The pervious test case cannot detect the change in the following code snippet.
```python
{mutant}
```
Generate a new test case to test the exception values in pervious code.
```python
# test case
def test():
    assert
    """

    return mutate_prompt


def read_csv(csv_path):
    #read csv file with pandas
    df = pd.read_csv(csv_path)
    return df

name_string= "T_O_FS_semticfixed_"
DATASET="HumanEval"
#DATASET="StudentEval"
#SCRIPT = str(1)
output_string ="test_oracle_FS_Mut_"
# CODE_DIR = os.path.join(
#                 os.getcwd(),
#                 DATASET,
#                 "Testing_" + DATASET, 
#                 "",
#             )

CODE_DIR = os.path.join(
                  os.getcwd(),
                DATASET,
                "Testing_" + DATASET,
                "",
            )

mut_dt = read_csv(os.path.join(CODE_DIR,  "fewshot_mutant_score.csv"))
mut_dt['lst_survived'] = mut_dt['lst_survived'].apply(lambda x: literal_eval(x) if "[" in x else x)

#print(mut_dt['MS'][0])

#for i, row in mut_dt.iterrows():
#81
i=160
row = mut_dt.iloc[141]

#SCRIPT = "q"+str(i+1)
SCRIPT = str(i+1)
print(row)
if row['MS'] <1 and row['is_problematic'] != 2:
    print(row['lst_survived'])


    SCRIPT_NAME =  name_string +SCRIPT+ ".py"
    print(SCRIPT_NAME)
    input_path = os.path.join(CODE_DIR , SCRIPT, "Codex", SCRIPT_NAME)

    with open(input_path) as input:
        function_to_test = input.read()

    lst_mut= row['lst_survived']
    print(lst_mut)
    j=0
    for mut in row['lst_survived']:
    #for mt in range(0,5):
        #mut = lst_mut[mt]
        print(mut)
        mutant_path = os.path.join(CODE_DIR, SCRIPT, "Mutants", mut)

        with open(mutant_path) as input:
            mutant_content = input.read()

        mutant_prompt = mutatePromptGenerator(function_to_test, mutant_content)
        print(mutant_prompt)
        model_output = call_LLMs(mutant_prompt, "```", 200) 
        print("inside function")
        print(model_output)
        print("############")


        output= function_to_test.split("def test():")
        code= output[0]
        test = output[1]
        file_content = code + "\ndef test():\n    " + model_output
        print(file_content)
        OUTPUT_NAME =  output_string + SCRIPT + "_"+ str(j) + ".py"
        output_path = os.path.join(CODE_DIR, SCRIPT, "Codex", OUTPUT_NAME)
        j +=1
        with open(output_path, "w") as output:
            output.write(file_content)
        output.close()



