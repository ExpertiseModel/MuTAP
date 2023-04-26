import os
import subprocess
from generate_test_oracle import synxtaxCheck


def check_test_oracle_sematic(function_to_correct):
    if not os.path.exists(os.path.join(os.getcwd(), "temp_dir")):
        os.mkdir(os.path.join(os.getcwd(), "temp_dir"))

    temp_dir_path = os.path.join(os.getcwd(),
                                 "temp_dir",
                                 )

    assert_dic=[]
    output= function_to_correct.split("def test():")
    code= output[0]

    if synxtaxCheck(function_to_correct):
        return code
    

    try:
        no_space= output[1].lstrip()
    except IndexError:
        print("no test")
        return code
    assert_lst= no_space.split("\n")
    assert_lst[0]= "    "+assert_lst[0]

    for ln in assert_lst:
        ln = ln.lstrip(' ')
        if ln.startswith("assert"):
            code_to_test = code +"\n" + ln.lstrip(' ')
            print(code_to_test)
            temp_test_script = open(
                        file=os.path.join(
                            temp_dir_path,
                            "temp_test_script.py",
                        ),
                        mode="w",
                    )

            temp_test_script.write(code_to_test)
            temp_test_script.close()
            try:
                result = subprocess.run(
                            [
                                "python3",
                                f"{os.path.join(temp_dir_path,'temp_test_script.py')}"
                            ], stdout = subprocess.PIPE, stderr = subprocess.PIPE, timeout=10
                        )
            
                print(result.returncode)
                # return code 0 means that the script ran without any errors
                if result.returncode == 0:
                    print("run with no error")       
                    assert_dic.append(0)
                elif result.returncode == 1:
                    print(result.stderr.decode("utf-8"))
                    if "AssertionError" in result.stderr.decode("utf-8"):
                        print("assertion error")
                        assert_dic.append(1)
                    else:
                        print("other error")
                        assert_dic.append(2)

            except subprocess.TimeoutExpired as e:
                assert_dic.append(3)
                print(e)
        else:
            print("no assert")
       
        

        

    final_test="def test():\n" 
    equal = 1             
    for i, item in enumerate(assert_dic):
        if item == 0:
            final_test += assert_lst[i] + "\n"

    print(final_test)
    print(assert_dic)

    all_content = code + "\n" + final_test

    return all_content



    



def apply_semantix_fix (DATASET, SCRIPT, script_string, output_string, csv_name):
    if DATASET == "StudentEval":
        CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Reference_Scripts", "Tests", 
                "",
            )
    else:
        CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Testing_" + DATASET, 
                "",
            )
    
    script_name = script_string + SCRIPT + ".py"
    input_path = os.path.join(CODE_DIR,  SCRIPT, "Codex", script_name)

    output_name = output_string + SCRIPT + ".py"
    output_path = os.path.join(CODE_DIR,  SCRIPT, "Codex", output_name)

   # csv_path = os.path.join(CODE_DIR, csv_name)
    
    file_name = input_path.split("/")[-1]

    with open(input_path) as input:
        function_to_correct = input.read()


    all_content = check_test_oracle_sematic(function_to_correct)

    with open(output_path, "w") as output:
        output.write(all_content)
    output.close()
        

    #with open(csv_path,'a') as csv_file:
       # csv_file.write(file_name + "," + str(total) + "," + str(semantic_fix))
      #  csv_file.write("\n")
   # csv_file.close()

    return ("done")





for i in range(1, 164):
   
    DATASET = "HumanEval"
    SCRIPT = str(i)
    script_string = "test_oracle_FS_"
    output_string = "fewshot_baseline_fixed_"
    csv_name = "normal_mut_all_semantic_fix.csv"
    CODE_DIR = os.path.join(
                    os.getcwd(),
                    DATASET,
                    "Testing_" + DATASET, 
                    "",
                )
        
    script_name = script_string + SCRIPT + ".py"
    print(script_name)
    input_path = os.path.join(CODE_DIR,  SCRIPT, "Codex", script_name)

    if os.path.exists(input_path):
        apply_semantix_fix("HumanEval",SCRIPT, script_string, output_string, csv_name)
    


# DATASET = "StudentEval"
# SCRIPT = "q"+str(5)
# script_string = "T_O_FS_Mut_all_"
# output_string = "T_O_FS_Mut_all_semticfixed_"
# csv_name = "st_fewshot_mut_all_semantic_fix.csv"
# CODE_DIR = os.path.join(
#                 os.getcwd(),
#                 DATASET,
#                 "Reference_Scripts", "Tests", 
#                 "",
#             )
    
# script_name = script_string + SCRIPT + ".py"
# input_path = os.path.join(CODE_DIR,  SCRIPT, "Codex", script_name)

# if os.path.exists(input_path):
#     apply_semantix_fix(DATASET,SCRIPT, script_string, output_string, csv_name)
    
