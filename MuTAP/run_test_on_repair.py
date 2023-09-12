import os
import subprocess
import pandas as pd

script_string = "T_O_NDS_semticfixed_"

result_dt = pd.DataFrame(columns = ["name" ,"status"])

def paths_list(dir_path):
   # dir_path = ques_dir_path + path_hlp 
    path_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path + "/" + file_name
        path_list.append(code_path)

    return path_list


DATASET = "StudentEval"
SCRIPT = "q"+str(3)
CODE_DIR = os.path.join(
                  os.getcwd(),
                  DATASET,
                "Reference_Scripts", 
                "",
            )
        
repair_paths = os.path.join(CODE_DIR, "Repair_st", SCRIPT)
lst_repair= paths_list(repair_paths)
all_repair = len(lst_repair)

test_NAME =  script_string + SCRIPT + ".py"
test_PATH = os.path.join(CODE_DIR,  "Tests", SCRIPT, "Codex", test_NAME)

num_pass =0 


if not os.path.exists(os.path.join(os.getcwd(), "temp_dir")):
        os.mkdir(os.path.join(os.getcwd(), "temp_dir"))


temp_dir_path = os.path.join(
        os.getcwd(),
        "temp_dir",
    )

with open(test_PATH) as input:
     code_to_content = input.read()


output= code_to_content.split("def test():")
try:
    code= output[0]
    test = output[1]

    for repair_path in lst_repair:
        file_name = repair_path.split("/")[-1]
        if "refactory_online_st"  in file_name:
                continue
    
        with open(repair_path, "r") as f:
            repair_content = f.read()

            all_content = repair_content +"def test():\n" + test + "\n" + "test()"
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
                    num_pass += 1
                    status = "pass"
                else:
                      status = "fail"

                result_dt= result_dt.append({"name": file_name, "status": status}, ignore_index=True) 
                print(file_name, status)

            except subprocess.TimeoutExpired as e:
                        print(file_name, "timeout")

except IndexError:
        print("No test function")


pass_perc = num_pass/(all_repair-1)
       
print("num_pass", pass_perc)

repair_csv_path = repair_paths + "/repair_stat.csv"
result_dt.to_csv(repair_csv_path, mode='a', index=False, header=False)