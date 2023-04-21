import os, subprocess, time


def human_eval_pynguing_test_generator():
    problematics = [
        10,
        12,
        13,
        25,
        32,
        39,
        55,
        59,
        63,
        75,
        76,
        81,
        92,
        95,
        99,
        106,
        111,
        123,
        124,
        127,
        139,
        140,
        141,
        142,
        143,
        144,
        147,
        148,
        156,
    ]
    for num in range(102, 103):
        if num not in problematics:
            DATASET = "HumanEval"
            SCRIPT = str(num)

            CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Testing_" + DATASET,
                SCRIPT,
                "",
            )

            SCRIPT_NAME = "script_" + SCRIPT

            os.makedirs(os.path.join(CODE_DIR, "Pynguin"), exist_ok=True)
            # run the commands necessary to generate the tests with Pynguin
            env_vairable = f"export PYNGUIN_DANGER_AWARE=True"
            python_seed = f"export PYTHONHASHSEED=0"
            command = f"{env_vairable};{python_seed};pynguin --project-path {CODE_DIR} --output-path {os.path.join(CODE_DIR, 'Pynguin')} --module-name {SCRIPT_NAME} --seed 42"
            # run this command in the terminal using subprocess
            # print time in blue
            print("\033[94m" + str(time.time()) + "\033[0m")
            # print command in green
            print("\033[92m" + command + "\033[0m")
            output = subprocess.run(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            print("\033[94m" + str(time.time()) + "\033[0m")
            # print the output of the command so that we know what is going on
            print(output.stdout.decode("utf-8"))


def code_contest_pynguing_test_generator():
    problematics = []

    DATASET = "CodeContest"
    problems = sorted(
        os.listdir(os.path.join(os.getcwd(), DATASET, "Testing_" + DATASET))
    )
    if ".DS_Store" in problems:
        problems.remove(".DS_Store")
    for problem in problems:
        if problem not in problematics:
            solutions = sorted(
                [
                    script
                    for script in os.listdir(
                        os.path.join(os.getcwd(), DATASET, "Testing_" + DATASET, problem)
                    )
                    if "_cp" not in script
                ]
            )

            for solution in solutions:

                CODE_DIR = os.path.join(
                    os.getcwd(),
                    DATASET,
                    "Testing_" + DATASET,
                    problem,
                    "",
                )

                SCRIPT_NAME = solution.replace(".py", "")

                os.makedirs(os.path.join(CODE_DIR, "Pynguin"), exist_ok=True)
                # run the commands necessary to generate the tests with Pynguin
                env_vairable = f"export PYNGUIN_DANGER_AWARE=True"
                python_seed = f"export PYTHONHASHSEED=0"
                command = f"{env_vairable};{python_seed};pynguin --project-path '{CODE_DIR}' --output-path '{os.path.join(CODE_DIR, 'Pynguin')}' --module-name '{SCRIPT_NAME}' --seed 42"
                # run this command in the terminal using subprocess
                # print time in blue
                print("\033[94m" + str(time.time()) + "\033[0m")
                # print command in green
                print("\033[92m" + command + "\033[0m")
                output = subprocess.run(
                    command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                print("\033[94m" + str(time.time()) + "\033[0m")
                # print the output of the command so that we know what is going on
                print(output.stdout.decode("utf-8"))


def student_eval_pynguing_test_generator():
    problematics = [2]
    for num in range(1, 6):
        if num not in problematics:
            DATASET = "StudentEval"
            SUB_DATASET = "Reference_Scripts"
            SCRIPT_NUM = str(num)

            CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                SUB_DATASET,
                "Scripts",
                "",
            )

            TEST_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                SUB_DATASET,
                "Tests",
                "",
            )
            SCRIPT_NAME = f"q{SCRIPT_NUM}"

            os.makedirs(os.path.join(TEST_DIR, SCRIPT_NAME, "Pynguin"), exist_ok=True)
            # run the commands necessary to generate the tests with Pynguin
            env_vairable = f"export PYNGUIN_DANGER_AWARE=True"
            python_seed = f"export PYTHONHASHSEED=0"
            command = f"{env_vairable};{python_seed};pynguin --project-path {CODE_DIR} --output-path {os.path.join(TEST_DIR,SCRIPT_NAME, 'Pynguin')} --module-name {SCRIPT_NAME} --seed 42"
            # run this command in the terminal using subprocess
            # print time in blue
            print("\033[94m" + str(time.time()) + "\033[0m")
            # print command in green
            print("\033[92m" + command + "\033[0m")
            output = subprocess.run(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            print("\033[94m" + str(time.time()) + "\033[0m")
            # print the output of the command so that we know what is going on
            print(output.stdout.decode("utf-8"))


human_eval_pynguing_test_generator()
