import os
import shutil

#80-100, 106, 110-112, 114, 117-164
for num in range(119, 164):
        DATASET = "HumanEval"
        SCRIPT = str(num)

        CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Testing_" + DATASET,
                SCRIPT,
                "",
            )
        
        TEST_NAME = "test_" + SCRIPT + "_cp_few_shot.py"
        test_path = os.path.join(CODE_DIR, 'Copilot', TEST_NAME)

        SCRIPT_NAME_normal = "script_" + SCRIPT + "_cp_normal.py"
        SCRIPT_NAME_fewshot = "script_" + SCRIPT + "_cp_few_shot.py"

        old_path_notmal = os.path.join(CODE_DIR, SCRIPT_NAME_normal)
        old_path_fewshot = os.path.join(CODE_DIR, SCRIPT_NAME_fewshot)


        new_path_notmal = os.path.join(CODE_DIR, 'Copilot', SCRIPT_NAME_normal)
        new_path_fewshot = os.path.join(CODE_DIR, 'Copilot', SCRIPT_NAME_fewshot)

        with open(test_path,'r+') as file:
            file.truncate(0)

        shutil.move(old_path_notmal, new_path_notmal)
        shutil.move(old_path_fewshot, new_path_fewshot)