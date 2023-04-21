import os, subprocess

main_path = os.path.join(
    os.getcwd(),
    "HumanEval",
    "Testing_HumanEval",
)

if not os.path.exists(os.path.join(os.getcwd(), "HumanEval", "ans")):
    os.mkdir(
        os.path.join(
            os.getcwd(),
            "HumanEval",
            "ans",
        )
    )
results_path = os.path.join(
    os.getcwd(),
    "HumanEval",
    "ans",
)

if not os.path.exists(
    os.path.join(
        os.getcwd(),
        "temp_dir",
    )
):
    os.mkdir(
        os.path.join(
            os.getcwd(),
            "temp_dir",
        )
    )
temp_dir_path = os.path.join(
    os.getcwd(),
    "temp_dir",
)

results_csv = open(
    file=os.path.join(
        results_path,
        f"pynguin_results.csv",
    ),
    mode="w",
)
results_csv.write("code_id,status,num_of_tests,num_of_pass,num_of_fail\n")

for script_num in range(1, 164):
    pynguin_tests_script_path = os.path.join(
        main_path,
        str(script_num),
        "Pynguin",
    )
    mutants_script_path = os.path.join(
        main_path,
        str(script_num),
        "Mutants",
    )
    try:
        test_script = open(
            os.path.join(
                pynguin_tests_script_path,
                f"test_script_{script_num}.py",
            ),
            "r",
        ).read()
    except FileNotFoundError:
        continue
    for mutant_script in os.listdir(mutants_script_path):
        if mutant_script.split(".")[1] != "py":
            continue
        mutant_script_contents = open(
            os.path.join(
                mutants_script_path,
                mutant_script,
            ),
            "r",
        ).read()

        temp_mutant_code = open(
            file=os.path.join(temp_dir_path, f"script_{script_num}.py"),
            mode="w",
        )
        temp_mutant_code.write(mutant_script_contents)
        temp_mutant_code.close()

        test_scripts = test_script.split("def")

        if len(test_scripts) == 2:
            temp_test_script = open(
                file=os.path.join(temp_dir_path, f"temp_test_script.py"),
                mode="w",
            )
            temp_test_script.write(test_script + "\ntest_case_0()")
            temp_test_script.close()
            try:
                status = "Pass"
                num_of_tests = len(test_scripts) - 1
                num_of_pass = 0
                num_of_fail = 0
                # We need to watch for timeout errors
                result = subprocess.run(
                    [
                        "python",
                        f"{os.path.join(temp_dir_path,'temp_test_script.py')}",
                    ],
                    capture_output=True,
                    timeout=10,
                )

                # return code 0 means that the script ran without any errors
                if result.returncode == 0:
                    print(
                        "\033[93m"
                        + f"{script_num}_{mutant_script}"
                        + "\033[92m"
                        + " - > Script Passed Without Errors"
                        + "\033[0m"
                    )
                    num_of_pass += 1
                elif result.returncode == 1:
                    # Assertion error means that the test failed
                    if "AssertionError" in result.stderr.decode("utf-8"):
                        print(
                            "\033[93m"
                            + f"{script_num}_{mutant_script}"
                            + "\033[91m"
                            + " - > Script Failed Assertion"
                            + "\033[0m"
                        )
                    # other errors means that the script failed with errors
                    else:
                        print(
                            "\033[93m"
                            + f"{script_num}_{mutant_script}"
                            + "\033[91m"
                            + " - > Script Failed With Errors"
                            + "\033[0m"
                        )

                    num_of_fail += 1
                    status = "Fail"
                else:
                    print(
                        "\033[91m"
                        + f"{script_num}_{mutant_script}"
                        + "\033[91m"
                        + " - > ERRRRRRRROR"
                        + "\033[0m"
                    )
            # I'll consider timeout as failing the test
            except subprocess.TimeoutExpired:
                print(
                    "\033[93m"
                    + f"{script_num}_{mutant_script}"
                    + "\033[94m"
                    + " - > Script Timed Out"
                    + "\033[0m"
                )
                num_of_fail += 1
                status = "Fail"

            results_csv.write(
                f"{script_num}_{mutant_script}"
                + ","
                + status
                + ","
                + str(num_of_tests)
                + ","
                + str(num_of_pass)
                + ","
                + str(num_of_fail)
                + "\n"
            )
        else:
            status = "Pass"
            num_of_tests = len(test_scripts) - 1
            num_of_pass = 0
            num_of_fail = 0

            for i in range(1, len(test_scripts)):
                temp_test_script = open(
                    file=os.path.join(
                        temp_dir_path,
                        "temp_test_script.py",
                    ),
                    mode="w",
                )
                # write each test to the temporary file
                temp_test_script.write(
                    "def".join(
                        [
                            test_scripts[0],
                            test_scripts[i] + f"\ntest_case_{i-1}()",
                        ],
                    )
                )
                temp_test_script.close()

                try:
                    result = subprocess.run(
                        [
                            "python",
                            f"{os.path.join(temp_dir_path,'temp_test_script.py')}",
                        ],
                        capture_output=True,
                        timeout=10,
                    )

                    # return code 0 means that the script ran without any errors
                    if result.returncode == 0:
                        print(
                            "\033[93m"
                            + f"{script_num}_{mutant_script}"
                            + "\033[92m"
                            + " - > Script Passed Without Errors"
                            + "\033[0m"
                        )
                        num_of_pass += 1

                    elif result.returncode == 1:
                        if "AssertionError" in result.stderr.decode("utf-8"):
                            print(
                                "\033[93m"
                                + f"{script_num}_{mutant_script}"
                                + "\033[91m"
                                + " - > Script Failed Assertion"
                                + "\033[0m"
                            )
                        # other errors means that the script failed with errors
                        else:
                            print(
                                "\033[93m"
                                + f"{script_num}_{mutant_script}"
                                + "\033[91m"
                                + " - > Script Failed With Errors"
                                + "\033[0m"
                            )
                        status = "Fail"
                        num_of_fail += 1
                # I'll consider timeout as failing the test
                except subprocess.TimeoutExpired:
                    print(
                        "\033[93m"
                        + f"{script_num}_{mutant_script}"
                        + "\033[94m"
                        + " - > Script Timed Out"
                        + "\033[0m"
                    )
                    num_of_pass += 1

            results_csv.write(
                f"{script_num}_{mutant_script}"
                + ","
                + status
                + ","
                + str(num_of_tests)
                + ","
                + str(num_of_pass)
                + ","
                + str(num_of_fail)
                + "\n"
            )
