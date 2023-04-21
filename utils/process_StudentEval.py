import os

# Path to the directory containing the HumanEval dataset
DS_PATH = os.path.join(os.getcwd(), "StudentEval", "Reference_Scripts","Scripts")
scripts = sorted(os.listdir(DS_PATH))

# for each script, read it and remove the tests in it
for script in scripts:
    script_contents = open(os.path.join(DS_PATH, script), "r").read()
    # The codes are all in the form of different functions
    # We want to let go of the test function which is always the last one
    # We need to keep the import statemtns if they are present
    script_funcs = [
        script
        for i, script in enumerate(script_contents.split("def"))
        if not (script.startswith("import") or script.startswith("from")) and not script.startswith("\n")
    ]
    # Separate the import statements from the rest of the code
    imports = (
        script_contents.split("def")[0] if script_contents.startswith("import") else ""
    )
    
    from_imports = (script_contents.split("def")[0] if script_contents.startswith("from") else "")
    # If there are any imports in the script, add them to the top of the script
    if imports != "":
        whole_script = script_funcs.insert(0, imports)
    
    if from_imports!="":
        whole_script = script_funcs.insert(0,from_imports)    

    # stich everything together
    s = ""
    for script_func in script_funcs:
        s += script_func
    # for generating the test cases
    # the normal one just has the prompt added at the end of it
    # the few shot one the csript should be inserted at #enter the new code here
    s_cp_normal = s + "\n # generate test case for the function above"
    s_cp_few_show = open(
        os.path.join(os.getcwd(), "utils", "few_shot_template.txt"), "r"
    ).read()

    s_cp_few_show = s_cp_few_show.replace("#enter the new code here", s)

    # save the script
    file_path = os.path.join(
        os.getcwd(),
        "StudentEval",
        "Reference_Scripts",
        "Tests",
        script.replace(".py", ""),
    )
    file_name = os.path.join(file_path, "script_"+script)
    file_name_cp_normal = os.path.join(file_path, "script_"+script.replace(".py","") + "_cp_normal"+".py")
    file_name_cp_few_shot = os.path.join(file_path, "script_"+script.replace(".py","") + "_cp_few_shot"+".py")

    os.makedirs(
        os.path.dirname(file_name),
        exist_ok=True,
    )
    
    with open(file_name, "w") as f:
        f.write(s)
    with open(file_name_cp_normal, "w") as f:
        f.write(s_cp_normal)
    with open(file_name_cp_few_shot, "w") as f:
        f.write(s_cp_few_show)


    