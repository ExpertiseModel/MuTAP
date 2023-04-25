import os
import subprocess
import sys

def check_test_oracle_sematic(function_to_correct):
    if not os.path.exists(os.path.join(os.getcwd(), "temp_dir")):
        os.mkdir(os.path.join(os.getcwd(), "temp_dir"))

    temp_dir_path = os.path.join(os.getcwd(),
                                 "temp_dir",
                                 )

    assert_dic=[]
    output= function_to_correct.split("def test():")
    code= output[0]
    try:
        no_space= output[1].lstrip()
    except IndexError:
        print("no test")
        return code, 0, 0 
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
        elif item == 1 or 2:
            asrt= assert_lst[i].lstrip()
            test_string = asrt[7:]
            if "==" in test_string:
                split_test = test_string.split('==')
            elif "is" in test_string:
                equal= 0
                split_test = test_string.split('is')
            input = split_test[0]
            output = split_test[1]
            code_to_test = code +"\n" + "print("+ input.lstrip(' ')+")"
            temp_test_script = open(
                        file=os.path.join(
                            temp_dir_path,
                            "temp_test_script.py",
                        ),
                        mode="w",
                    )

            temp_test_script.write(code_to_test)
            temp_test_script.close()
            result = subprocess.run(
                            [
                                "python3",
                               f"{os.path.join(temp_dir_path,'temp_test_script.py')}"
                            ], stdout = subprocess.PIPE, stderr = subprocess.PIPE, timeout=10
                        )
            if result.returncode == 0:
                output = result.stdout.decode("utf-8")
                if equal == 0:
                    final_test += "    assert " + input + "is " + output
                else:
                    final_test += "    assert " + input + "== " + output

            else:
                final_test += assert_lst[i]

    print(final_test)
    print(assert_dic)

    all_content = code + "\n" + final_test

    semantic_fix = assert_dic.count(1)
    total = len(assert_dic)

    return all_content, semantic_fix, total



    



def apply_semantix_fix (DATASET, SCRIPT, script_string, output_string, csv_name):
    if DATASET == "Refactory":
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

    csv_path = os.path.join(CODE_DIR, csv_name)
    
    file_name = input_path.split("/")[-1]

    with open(input_path) as input:
        function_to_correct = input.read()


    all_content, semantic_fix, total = check_test_oracle_sematic(function_to_correct)

    with open(output_path, "w") as output:
        output.write(all_content)
    output.close()
        

    with open(csv_path,'a') as csv_file:
        csv_file.write(file_name + "," + str(total) + "," + str(semantic_fix))
        csv_file.write("\n")
    csv_file.close()

    return ("done")


    
def main():
    arguments = sys.argv
    if len(arguments) != 6:
        raise SystemExit('6 inputs are required: semantic_err_correction.py [dataset] [task_num] [input prefix name] [output prefix name] [csv report filename (.csv)]')
    else:
        DATASET = arguments[1]
        task_num = arguments[2]
        input_string = arguments[3]
        output_string = arguments[4]
        semantic_report = arguments[5]


        
        if os.path.splitext(semantic_report)[1] == ".csv":
            if DATASET == "HumanEval":
                CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Testing_" + DATASET, 
                "",
                )
                script_name = input_string + task_num + ".py"
                input_path = os.path.join(CODE_DIR,  task_num, "Codex", script_name)  
                if os.path.exists(input_path):
                    apply_semantix_fix(DATASET,task_num, input_string, output_string, semantic_report)

            elif DATASET == "Refactory":
                CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Reference_Scripts", "Tests", 
                "",
                )
                SCRIPT_num = "q"+str(task_num)
                script_name = input_string + SCRIPT_num + ".py"
                input_path = os.path.join(CODE_DIR,  SCRIPT_num, "Codex", script_name)  
                if os.path.exists(input_path):
                    apply_semantix_fix(DATASET, SCRIPT_num, input_string, output_string, semantic_report)

            else:
                raise SystemExit("Error : Dataset name is not valid")
        else:
            raise SystemExit("Error : the report file should be a csv")

if __name__ == '__main__':
    main()





    
