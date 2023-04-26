import os
import sys


def paths_list(dir_path):
   # dir_path = ques_dir_path + path_hlp 
    path_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path + "/" + file_name
        path_list.append(code_path)

    return path_list

def merge_asserts(file_path):
    test_content = ""

    with open(file_path) as input:
        content = input.read()
    content = content.split("def test():")
    code = content[0]
    try:
        test= content[1].lstrip()
    except IndexError:
        print("no test")
        return  test_content
    
    assert_lst= test.split("\n")
    #assert_lst[0]= "    "+assert_lst[0]
    
    for ln in assert_lst:
        ln= ln.lstrip(' ')
        if ln.startswith("assert") and len(ln)> 10:
            test_content = test_content  + "    "+ ln.lstrip(' ')+"\n"

    return test_content

def Mut_all_in_one (DATASET, SCRIPT, code_string, script_string, output_string):

    CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Testing_" + DATASET, 
                "",
            )
    Script_path = os.path.join(CODE_DIR,  SCRIPT, "Codex")

    code_name =  code_string + SCRIPT + ".py"
    code_path = os.path.join(CODE_DIR,  SCRIPT, "Codex", code_name)

    with open(code_path) as input:
        function_to_test = input.read()
    
    output= function_to_test.split("def test():")
    code= output[0]
    try:
        test = output[1]
    except IndexError:
        print("no test")
        test= ""

    OUTPUT_NAME =  output_string + SCRIPT + ".py"
    OUTPUT_PATH = os.path.join(CODE_DIR, SCRIPT, "Codex", OUTPUT_NAME)

    lst_script= paths_list(Script_path)
    
    test_content_after_mut = ""
    for script in lst_script:
        script_name = script.split("/")[-1]
        if script_name.startswith(script_string):
            single_test_content = merge_asserts(script)
            if single_test_content != "":
                test_content_after_mut= test_content_after_mut +  merge_asserts(script) + "\n"

            
    all_content_after_mut = code + "\ndef test():\n" + test + test_content_after_mut

    with open(OUTPUT_PATH, "w") as output:
        output.write(all_content_after_mut)
    output.close()

    print(OUTPUT_NAME)
    return (OUTPUT_NAME +"\n")


def main():
    arguments = sys.argv
    if len(arguments) != 6:
        raise SystemExit('6 inputs are required: Merge_all_mut.py [dataset] [task_num] [inital test name] [augmented test name] [output name]')
    else:
        DATASET = arguments[1]
        task_num = arguments[2]
        IUT = arguments[3]
        AUT = arguments[4]
        output_namr = arguments[5]

        
        if DATASET == "HumanEval":
            Mut_all_in_one (DATASET, str(task_num), IUT, AUT, output_namr) 

        elif DATASET == "Refactory":
            SCRIPT_num = "q"+str(task_num)
            Mut_all_in_one (DATASET, SCRIPT_num, IUT, AUT, output_namr) 

        else:
            raise SystemExit("Error : Dataset name is not valid")
        
if __name__ == '__main__':
    main()


         


 