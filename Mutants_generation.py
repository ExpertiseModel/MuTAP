import os
import subprocess, time

def Generate_Mutants():
    for num in range(1, 6):
       # DATASET = "HumanEval"
        #SCRIPT = str(num)

        #CODE_DIR = os.path.join(
            #     os.getcwd(),
            #     DATASET,
            #     "Testing_" + DATASET,
            #     SCRIPT,
            #     "",
            # )

        DATASET = "StudentEval"
        SCRIPT = "q"+str(num)

        CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Reference_Scripts", "Tests",
                SCRIPT,
                "",
            )
        
        #SCRIPT_NAME = "script_NDS_" + SCRIPT + ".py"
        SCRIPT_NAME = "script_" + SCRIPT + ".py"
        #TEST_NAME = "test_" + SCRIPT + "_cp_few_shot.py"
        TEST_NAME = "script_" + SCRIPT + "_cp_few_shot.py"

        target_path = os.path.join(CODE_DIR, SCRIPT_NAME)
        #test_path = os.path.join(CODE_DIR, 'Copilot', TEST_NAME)
        test_path = os.path.join(CODE_DIR, TEST_NAME)

        os.makedirs(os.path.join(CODE_DIR, "Mutants"), exist_ok=True)
        
        OUT_NAME = "mutants_all_" + SCRIPT + ".txt"
        command = f"mut.py --target {target_path} --unit-test {test_path} -m > {os.path.join(CODE_DIR, 'Mutants', OUT_NAME)}"

        print("\033[92m" + command + "\033[0m")

        try:
            output = subprocess.run(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
        except:
            print("file not found: " + SCRIPT)
        
        print(output.stdout.decode("utf-8"))



def Seperate_Mutants():
    for num in range(1, 5):
        # DATASET = "HumanEval"
        # SCRIPT = str(num)

        # CODE_DIR = os.path.join(
        #         os.getcwd(),
        #         DATASET,
        #         "Testing_" + DATASET,
        #         "",
        #     )
        
        # SCRIPT_NAME = "script_NDS_" + SCRIPT + ".py"
        DATASET = "StudentEval"
        SCRIPT = "q"+str(num)

        CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Reference_Scripts", "Tests",
                "",
            )
        
        SCRIPT_NAME = "script_" + SCRIPT + ".py"
        MUTANT_NAME = "mutants_all_" + SCRIPT + ".txt"

        SCRIPT_PATH = os.path.join(CODE_DIR, SCRIPT, SCRIPT_NAME)
        MUTANT_PATH = os.path.join(CODE_DIR, SCRIPT, "Mutants")

        csv_path = os.path.join(CODE_DIR, "st_mutant_type.csv")

        i=0
        try:
            with open( SCRIPT_PATH ,'r',encoding='utf-8') as file:
                org_data = file.readlines()
                file.close()
            with open(os.path.join(MUTANT_PATH, MUTANT_NAME), 'r') as f:
                for ln in f:
                    ln = ln.lstrip(' ')
                    if ln.startswith("- [#"):
                        ln_mut = ln.split()
                        mut_type = ln_mut[3]
                    if ln.startswith("+"):
                        ln_partition = ln.split(":")
                        ln_num = (ln_partition[0][1:]).lstrip(' ')
                        ln_content= ln[6:]
                        #print(org_data)
                        temp = org_data[:]
                        temp[int(ln_num) -1 ] = ln_content
                        #print(org_data)
                        name = "mutant_" + SCRIPT +"_" + str(i)+".py"
                        SUB_MU_NAME = os.path.join(MUTANT_PATH, name)
                        mutant = open(SUB_MU_NAME, 'w')
                        for item in temp:
                            mutant.write(item)
                        mutant.close()

                        with open(csv_path,'a') as csv_file:
                            csv_file.write(name + "," + str(mut_type))
                            csv_file.write("\n")
                            csv_file.close()
                        i+=1
                        print("generate mutant: " + name)
        except Exception as e:
            print("file not found: " + e)



if __name__ == "__main__":
   # Generate_Mutants()
    Seperate_Mutants()