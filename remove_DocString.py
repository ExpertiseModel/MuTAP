import ast  
import re
import os
from Mutation_Score import paths_list

for i in range(102, 167):
     DATASET = "HumanEval"
     SCRIPT = str(i)
     CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Testing_" + DATASET,
                SCRIPT,
                "",
            )
     
     Mutant_PATH = os.path.join(CODE_DIR, "Mutants")
     mutant_lst = paths_list(Mutant_PATH)
     
     for path in mutant_lst:
        with open(path) as input_file:
            file_name = path.split("/")[-1]
            print (file_name)
            if "all"  in file_name:
                continue
            file_content = input_file.read()
        input_file.close()


        data_ls = file_content.split('METADATA')

        remove_str= re.sub(r'(\"{2,3}[\s\n]*)(?:.*?[\s\n]*)*([\n\s]*\"{2,3})', r'', data_ls[0], flags=re.MULTILINE)


        print(data_ls[0])
        print(remove_str)
     


        with open(path, 'w') as output_file:
            output_file.write(remove_str)
        output_file.close()

