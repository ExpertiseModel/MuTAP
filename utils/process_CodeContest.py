import os
import pickle

# directories
DS_PATH = os.path.join(os.getcwd(), "CodeContest_original", "output_py_train")
ORIGINAL_DS_SAVE_PATH = os.path.join(os.getcwd(), "CodeContest", "Original_Dataset")
PROCESSED_DS_SAVE_PATH = os.path.join(os.getcwd(), "CodeContest", "Testing_CodeContest")

# since this dataset has multiple solutions for each problem and it has a loooot problems,
# we need to set a limit on how many problems we want to use
scripts = sorted(os.listdir(DS_PATH))
script_limit = 1
solution_limit = 1

# load the few shot template
few_shot_cp_test_template = open(
    os.path.join(os.getcwd(), "utils", "few_shot_template.txt"), "r"
).read()

# for each of the pickle files
for pickel_file in scripts:
    file = open(os.path.join(DS_PATH, pickel_file), "rb")
    file = pickle.load(file)

    for k, solution in file["solutions"].items():
        # original code
        code_description = r'"""' + file["description"] + r'"""'
        # code with prompt added
        normal_cp_test = "\n\n# generate test case for the function above"

        # set the save path of processed scripts
        j = os.path.join(
            os.getcwd(),
            PROCESSED_DS_SAVE_PATH,
            pickel_file.replace(".pickle", ""),
        )

        os.makedirs(
            os.path.join(
                os.getcwd(),
                PROCESSED_DS_SAVE_PATH,
                pickel_file.replace(".pickle", ""),
            ),
            exist_ok=True,
        )

        # save the original code
        with open(
            os.path.join(
                j,
                (f"{k}_" + pickel_file).replace(".pickle", ".py").replace(". ", "_"),
            ),
            "w",
        ) as f:

            f.write(code_description + "\n\n" + solution)
        # save the code with copilot prompt added
        with open(
            os.path.join(
                j,
                (
                    f"{k}_"
                    + pickel_file.replace(".pickle", "").replace(". ", "_")
                    + "_cp_normal"
                    + ".py"
                ),
            ),
            "w",
        ) as f:
            f.write(code_description + "\n\n" + solution + normal_cp_test)
        # save the code with few_shot template
        with open(
            os.path.join(
                j,
                (
                    f"{k}_"
                    + pickel_file.replace(".pickle", "").replace(". ", "_")
                    + "_cp_few_shot"
                    + ".py"
                ),
            ),
            "w",
        ) as f:
            f.write(
                few_shot_cp_test_template.replace("#enter the new code here", solution)
                + normal_cp_test
            )

        solution_limit += 1
        if solution_limit == 5:
            solution_limit = 1
            break

    script_limit += 1
    if script_limit == 10:
        solution_limit = 1
        break
