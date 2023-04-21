
import os
import subprocess
from generate_test_oracle import synxtaxCheck

def paths_list(dir_path):
   # dir_path = ques_dir_path + path_hlp 
    path_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path + "/" + file_name
        path_list.append(code_path)

    return path_list

def count_solved(DATASET, SCRIPT, script_string):
    solved = 0
    CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Testing_" + DATASET, SCRIPT, "Codex",
                "",
            )

    SCRIPT_NAME = script_string + SCRIPT + ".py"
    SCRIPT_PATH = os.path.join(CODE_DIR, SCRIPT_NAME)


    with open(SCRIPT_PATH) as input:
        function_to_correct = input.read()

    output= function_to_correct.split("def test():")
    try:
        no_space= output[1].lstrip()
        solved=1

    except IndexError:
        return solved

    return solved

def count_mutant_run(DATASET, SCRIPT, script_string):
    solved = 0
    CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Testing_" + DATASET, SCRIPT, "Codex",
                "",
            )

    lst_script= paths_list(CODE_DIR)
    
    mut_run = 0
    synx_error = 0
    for script in lst_script:
        script_name = script.split("/")[-1]
        if script_name.startswith(script_string):
            mut_run +=1
            with open(script) as input:
                function_to_correct = input.read()
                if synxtaxCheck(function_to_correct):
                    synx_error +=1


    return mut_run, synx_error


DATASET ="HumanEval"
#SCRIPT = str(3)
script_string = "fewshot_baseline_fixed_"
csv_name= "fewshot_mut_all_synx.csv"
solved_prob= 0
for i in range(1, 164):
    SCRIPT = str(i)
    solved_prob = solved_prob + count_solved(DATASET, SCRIPT, script_string)

print(solved_prob)


# for i in range(1,  164):
#     SCRIPT = str(i)
#     Script_name = script_string + SCRIPT + ".py"
#     csv_path = os.path.join(
#                 os.getcwd(),
#                 DATASET,
#                 "Testing_" + DATASET, csv_name
#             )
#     mut_num, syx_err= count_mutant_run(DATASET, SCRIPT, script_string)

#     with open(csv_path,'a') as csv_file:
#         csv_file.write(Script_name + "," + str(mut_num) + "," + str(syx_err))
#         csv_file.write("\n")
#     csv_file.close()