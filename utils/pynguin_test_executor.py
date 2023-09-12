import os
import subprocess

# the path to the original script
original_script_path = os.path.join(
    os.getcwd(),
    "StudentEval",
    "Reference_Scripts",
    "Scripts",
)
# the path to the test scripts
test_script_path = os.path.join(
    os.getcwd(),
    "StudentEval",
    "Reference_Scripts",
    "Tests",
)
# the path to the student codes
student_code_path = os.path.join(
    os.getcwd(),
    "StudentEval",
    "Reference_Scripts",
    "Wrong_st",
)
# path to the results csv file
results_path = os.path.join(
    os.getcwd(),
    "StudentEval",
    "Reference_Scripts",
    "ans",
)
# the temprorary generated codes go here
if not os.path.exists(os.path.join(os.getcwd(), "temp_dir")):
    os.mkdir(os.path.join(os.getcwd(), "temp_dir"))

temp_dir_path = os.path.join(
    os.getcwd(),
    "temp_dir",
)

# We don't want to iterate over these files
problematics = [
    "__init__.py",
    "__pycache__","few_shot_query.py"
]
mode = "student"  # or original
# q1, q2, etc.
for script_name in sorted(os.listdir(test_script_path)):
    # read the content of the original script
    original_script = open(
        os.path.join(test_script_path, script_name, f"script_{script_name}.py"),
        "r",
    ).read()
    # read the content of the test script
    test_script = open(
        os.path.join(test_script_path, script_name, "Pynguin", f"test_{script_name}.py"),
        "r",
    ).read()
    # open the results csv file
    resluts_csv = open(
        file=os.path.join(
            results_path,
            script_name,
            f"pynguin_original_script_results.csv"
            if mode == "original"
            else f"pynguin_results.csv",
        ),
        mode="w",
    )
    resluts_csv.write("code_id,status,num_of_tests,num_of_pass,num_of_fail\n")
    # iterate over the student codes
    if mode == "student":
        for student_code_name in sorted(
            os.listdir(
                os.path.join(
                    student_code_path,
                    script_name,
                    "wrong",
                )
            )
        ):
            if student_code_name not in problematics:
                # read the content of the student code
                student_code = open(
                    file=os.path.join(
                        student_code_path,
                        script_name,
                        "wrong",
                        student_code_name,
                    ),
                    mode="r",
                ).read()

                # write the content of the student code to a temporary file
                temp_student_code = open(
                    file=os.path.join(
                        os.getcwd(),
                        "temp_dir",
                        f"{script_name}.py",
                    ),
                    mode="w",
                )
                temp_student_code.write(student_code)
                temp_student_code.close()
                # since each test script mioght contain multiple tests, split the tests by function definition
                test_scripts = test_script.split("def")
                # if there is only one test, then we don't need to split the test script

                if len(test_scripts) == 2:
                    temp_test_script = open(
                        file=os.path.join(
                            temp_dir_path,
                            "temp_test_script.py",
                        ),
                        mode="w",
                    )

                    # add calling the test function to the end of the test script so that we can run it
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
                                + student_code_name
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
                                    + student_code_name
                                    + "\033[91m"
                                    + " - > Script Failed Assertion"
                                    + "\033[0m"
                                )
                            # other errors means that the script failed with errors
                            else:
                                print(
                                    "\033[93m"
                                    + student_code_name
                                    + "\033[91m"
                                    + " - > Script Failed With Errors"
                                    + "\033[0m"
                                )

                            num_of_fail += 1
                            status = "Fail"
                        else:
                            print(
                                "\033[91m"
                                + student_code_name
                                + "\033[91m"
                                + " - > ERRRRRRRROR"
                                + "\033[0m"
                            )
                    # I'll consider timeout as failing the test
                    except subprocess.TimeoutExpired:
                        print(
                            "\033[93m"
                            + student_code_name
                            + "\033[94m"
                            + " - > Script Timed Out"
                            + "\033[0m"
                        )
                        num_of_fail += 1
                        status = "Fail"

                    resluts_csv.write(
                        student_code_name
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
                # if there are multiple tests, then we need to split the test script
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
                                    + student_code_name
                                    + "\033[92m"
                                    + " - > Script Passed Without Errors"
                                    + "\033[0m"
                                )
                                num_of_pass += 1

                            elif result.returncode == 1:
                                if "AssertionError" in result.stderr.decode("utf-8"):
                                    print(
                                        "\033[93m"
                                        + student_code_name
                                        + "\033[91m"
                                        + " - > Script Failed Assertion"
                                        + "\033[0m"
                                    )
                                # other errors means that the script failed with errors
                                else:
                                    print(
                                        "\033[93m"
                                        + student_code_name
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
                                + student_code_name
                                + "\033[94m"
                                + " - > Script Timed Out"
                                + "\033[0m"
                            )
                            num_of_pass += 1

                    resluts_csv.write(
                        student_code_name
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

    elif mode == "original":
        temp_original_code = open(
            file=os.path.join(
                os.getcwd(),
                "temp_dir",
                f"{script_name}.py",
            ),
            mode="w",
        )
        temp_original_code.write(original_script)
        temp_original_code.close()

        test_scripts = test_script.split("def")

        if len(test_scripts) == 2:
            temp_test_script = open(
                file=os.path.join(
                    temp_dir_path,
                    "temp_test_script.py",
                ),
                mode="w",
            )

            # add calling the test function to the end of the test script so that we can run it
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
                        + script_name
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
                            + script_name
                            + "\033[91m"
                            + " - > Script Failed Assertion"
                            + "\033[0m"
                        )
                    # other errors means that the script failed with errors
                    else:
                        print(
                            "\033[93m"
                            + script_name
                            + "\033[91m"
                            + " - > Script Failed With Errors"
                            + "\033[0m"
                        )

                    num_of_fail += 1
                    status = "Fail"
                else:
                    print(
                        "\033[91m"
                        + script_name
                        + "\033[91m"
                        + " - > ERRRRRRRROR"
                        + "\033[0m"
                    )
                    # I'll consider timeout as failing the test
            except subprocess.TimeoutExpired:
                print(
                    "\033[93m"
                    + script_name
                    + "\033[94m"
                    + " - > Script Timed Out"
                    + "\033[0m"
                )
                num_of_fail += 1
                status = "Fail"

            resluts_csv.write(
                script_name
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
            # if there are multiple tests, then we need to split the test script
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
                            + script_name
                            + "\033[92m"
                            + " - > Script Passed Without Errors"
                            + "\033[0m"
                        )
                        num_of_pass += 1

                    elif result.returncode == 1:
                        if "AssertionError" in result.stderr.decode("utf-8"):
                            print(
                                "\033[93m"
                                + script_name
                                + "\033[91m"
                                + " - > Script Failed Assertion"
                                + "\033[0m"
                            )
                        # other errors means that the script failed with errors
                        else:
                            print(
                                "\033[93m"
                                + script_name
                                + "\033[91m"
                                + " - > Script Failed With Errors"
                                + "\033[0m"
                            )
                        status = "Pass"
                        num_of_fail += 1
                # I'll consider timeout as failing the test
                except subprocess.TimeoutExpired:
                    print(
                        "\033[93m"
                        + script_name
                        + "\033[94m"
                        + " - > Script Timed Out"
                        + "\033[0m"
                    )
                    num_of_pass += 1

            resluts_csv.write(
                script_name
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
