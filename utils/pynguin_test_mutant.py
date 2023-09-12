import os
import subprocess
import pandas as pd

ROOT = os.getcwd()


def paths_list(dir_path):
    path_list = []
    for file_name in os.listdir(dir_path):
        if file_name.endswith(".py"):
            code_path = dir_path + "/" + file_name
            path_list.append(code_path)
    
    return path_list

if not os.path.exists(os.path.join(os.getcwd(), "temp_dir")):
    os.mkdir(os.path.join(os.getcwd(), "temp_dir"))

temp_dir_path = os.path.join(
    os.getcwd(),
    "temp_dir",
    
)

pynguin_mutant_results = pd.DataFrame(columns = ["code_id","MS","ls_pass"])
for i in range(1, 164):
    
       

    test_name= "test_script_" + str(i) + "_no_metadata.py"
    test_path = os.path.join(ROOT, "HumanEval", "Testing_HumanEval", str(i), "Pynguin", test_name)


    
    mutant_path = os.path.join(ROOT, "HumanEval", "Testing_HumanEval", str(i), "Mutants")
    mutant_code_lst = paths_list(mutant_path)
    all_mutants = len(mutant_code_lst)

    n_killed_mutants = 0
    survived_mutants =[]

    if os.path.exists(test_path):
        for script_path in sorted(mutant_code_lst):
            file_name = script_path.split("/")[-1]
            if "all"  in file_name:
                continue

            temp_code = open(
                file=os.path.join(temp_dir_path, f"script_{str(i)}.py"),
                mode="w",
            )

            buggy_script_contents = open(
                os.path.join(
                script_path
                ),
                "r",
                ).read()
            temp_code.write(buggy_script_contents)
            temp_code.close()
        
            
            # read the content of the test script
            test_script = open(test_path).read()
            # Taking into account annotation of PyTest ("@") in the split
            test_scripts = test_script.split("def")
            # Some element might be empty because of the above
            

            
            num_of_tests = len(test_scripts) - 1
            num_of_pass = 0
            num_of_fail = 0
            for j in range(1, len(test_scripts)):
                test_name_str= test_scripts[j].split(":")
                test_name_prf = test_name_str[0].lstrip()
                #test_name_final = test_name_prf.split("def")[1].lstrip()
                temp_test_script = open(file=os.path.join(
                                    temp_dir_path,
                                    "temp_test_script.py",
                                ),
                                mode="w",
                            )
                            # write each test to the temporary file
                # Joining with a new line not to mess up the test
                # Removing adding the line "test_case_X()" since we will use pytest
                temp_test_script.write("\ndef".join(
                                    [
                                        test_scripts[0],
                                        test_scripts[j]+"\n" + test_name_prf, # + f"\ntest_case_{j-1}()",
                                    ],
                                )
                            )
                temp_test_script.close()
                try: 
                    # Changing python3 -> pytest. Everything else should still work as intended
                    result = subprocess.run(
                                        [
                                            "python3",
                                        f"{os.path.join(temp_dir_path,'temp_test_script.py')}"
                                        ], stdout = subprocess.PIPE, stderr = subprocess.PIPE, timeout=10
                                    )
                    if result.returncode == 0:
                        #status = "pass"
                        num_of_pass += 1
                        print(script_path, ":pass")

                    else: 
                        #status = "fail"
                        num_of_fail += 1
                        print(script_path, ":fail")

                except subprocess.TimeoutExpired as e:
                    #status = "fail"
                    num_of_fail += 1
                    print(script_path, "timeout")
            
            if num_of_fail > 0:
                status = "fail"
                n_killed_mutants += 1

            else: 
                survived_mutants.append(file_name)

        try:   
            MS = n_killed_mutants/all_mutants

        except ZeroDivisionError:
            MS= "NA"
        dir_name = "HumanEval_" + str(i) 
        pynguin_mutant_results = pynguin_mutant_results.append({"code_id":dir_name,  "MS":MS, "ls_pass":survived_mutants}, ignore_index=True)
    else:
        print("no test script")

                
        

pynguin_result_failed_path = os.path.join(os.getcwd(), "pynguin_mutant_result.csv")
pynguin_mutant_results.to_csv(pynguin_result_failed_path, mode= 'a', index=False, header=False)