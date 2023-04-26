import os
import subprocess
import pandas as pd
import sys


def paths_list(dir_path):
   # dir_path = ques_dir_path + path_hlp 
    path_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path + "/" + file_name
        path_list.append(code_path)

    return path_list


def MS_generator (DATASET, SCRIPT, script_string, csv_name):

    result_dt = pd.DataFrame(columns = ["name" ,"MS","lst_survived","n_killed","n_all_mut","is_problematic","lst_problematic","lst_timeout","lst_killed"])
    
    if DATASET == "Refactory":
        CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Reference_Scripts", 
            )
        
        mutant_path = os.path.join(CODE_DIR, "Wrong_st", SCRIPT, "wrong")
        lst_mut= paths_list(mutant_path)
        all_mutants = len(lst_mut)

        SCRIPT_NAME =  script_string + SCRIPT + ".py"
        SCRIPT_PATH = os.path.join(CODE_DIR,  "Tests", SCRIPT, "Codex", SCRIPT_NAME)
    else:
        CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Testing_" + DATASET, 
                "",
            )
         
        mutant_path = os.path.join(CODE_DIR,  SCRIPT, "Mutants")
        lst_mut= paths_list(mutant_path)
        all_mutants = len(lst_mut)-1

        SCRIPT_NAME =  script_string + SCRIPT + ".py"
        SCRIPT_PATH = os.path.join(CODE_DIR,  SCRIPT, "Codex", SCRIPT_NAME)

    with open(SCRIPT_PATH) as input:
        code_to_content = input.read()

    

    mutation_csv_path = os.path.join(CODE_DIR, csv_name)


    if not os.path.exists(os.path.join(os.getcwd(), "temp_dir")):
        os.mkdir(os.path.join(os.getcwd(), "temp_dir"))


    temp_dir_path = os.path.join(
        os.getcwd(),
        "temp_dir",
    )

    n_survived_mutants = 0
    n_killed_mutants = 0
    survived_mutants =[]
    problematic_test = 0
    problematic_num = 0
    killed_list = []
    problematic_list = []
    timout_list = []

    output= code_to_content.split("def test():")
    try:
        code= output[0]
        test = output[1]

        for mut_path in lst_mut:
            with open(mut_path, "r") as f:
                    file_name = mut_path.split("/")[-1]
                    mut_content = f.read()
            if "all"  in file_name:
                continue
            all_content = mut_content +"def test():\n" + test + "\n" + "test()"
            temp_test_script = open(
                                file=os.path.join(
                                    temp_dir_path,
                                    "temp_test_script.py",
                                ),
                                mode="w",
                            )

            temp_test_script.write(all_content)
            temp_test_script.close()
            try: 
                result = subprocess.run(
                                    [
                                        "python3",
                                    f"{os.path.join(temp_dir_path,'temp_test_script.py')}"
                                    ], stdout = subprocess.PIPE, stderr = subprocess.PIPE, timeout=10
                                )
                if result.returncode == 0:
                    survived_mutants.append(file_name)
                    n_survived_mutants += 1

                elif result.returncode == 1:
                    if "AssertionError" in result.stderr.decode("utf-8"):
                        print(file_name, "assertion error")
                        killed_list.append(file_name)
                        n_killed_mutants += 1


                    else:
                        print(file_name,"other error")
                        #n_killed_mutants += 1
                        problematic_num += 1
                        problematic_list.append(file_name)
                        problematic_test=1

            except subprocess.TimeoutExpired as e:
                        problematic_test=1
                        problematic_num += 1
                        timout_list.append(file_name)
                        print(file_name, "timeout")

    except IndexError:
        print("No test function")
        problematic_test=2
        
    try:
         Mutation_score = n_killed_mutants/(all_mutants - problematic_num)

         #Mutation_score = n_killed_mutants/all_mutants 

         result_dt= result_dt.append({"name": SCRIPT_NAME, "MS": Mutation_score, "lst_survived": survived_mutants, 
                      "n_killed": n_killed_mutants, "n_all_mut": all_mutants, "is_problematic": problematic_test, "lst_problematic": problematic_list,
                      "lst_timeout": timout_list, "lst_killed": killed_list}, ignore_index=True)       
    except ZeroDivisionError:
         print("divided by zero")     
    
    #with open(mutation_csv_path,'a') as mut_file:
           # mut_file.write(SCRIPT_NAME + "," + str(Mutation_score) + "," + str(survived_mutants) + "," + str(n_killed_mutants) + "," + str(all_mutants) + "," +  str(problematic_test))
           # mut_file.write("\n")
    #mut_file.close()

    result_dt.to_csv(mutation_csv_path, mode='a', index=False, header=False)




def main():
    arguments = sys.argv
    if len(arguments) != 5:
        raise SystemExit('5 inputs are required: Mutation_Score.py [dataset] [task_num] [testfile prefix name] [csv report filename (.csv)]')
    else:
        DATASET = arguments[1]
        task_num = arguments[2]
        testfile_string = arguments[3]
        MS_report = arguments[4]

    if os.path.splitext(MS_report)[1] == ".csv":
          MS_generator(DATASET, task_num, testfile_string, MS_report)

    else:
         raise SystemExit("Error : the report file should be a csv")

if __name__ == '__main__':
    main()
