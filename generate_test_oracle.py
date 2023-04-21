import ast  
import re
import openai 
import os
#from Sematic_err_correction import check_test_oracle_sematic

openai.api_key = "My_key"
#a function to generate the intial prompt to call the model
def initalPromptGenerator(function_to_test):
    inital_prompt = f""" Generate test cases for
```python
{function_to_test}

# test case
def test():
    assert 
"""
    return inital_prompt

# a function to generate fewshot prompt to call the model
def fewshotPromptGenerator(fewshot_content,function_to_test):
    fewshot_prompt = f"""
{fewshot_content}

{function_to_test}

#</code>

#<test>

def test():
    assert 
"""
    return fewshot_prompt


# a function to generate the synx prompt to call the model incase there is a syntax error in the output of the model
def synxPromptGenerator(test_Oracle):
    synx_prompt = f""" Fix the syntax error the last line of the following code:
```python
{test_Oracle}

"""
    return synx_prompt



#check the syntax of the test oracle
def synxtaxCheck(test_oracle):
    try:
        ast.parse(test_oracle)
        return False
    except SyntaxError:
        return True
    
#fix the syntax erro of the test oracle by eliminating the lines with the error
def synxtaxfixer(test_oracle):
    try:
        ast.parse(test_oracle)
        return test_oracle
    except SyntaxError as e:
        line_to_rm = e.lineno
        lines = test_oracle.split("\n")
        if line_to_rm is None or line_to_rm >= len(lines):
            return synxtaxfixer("\n".join(lines[:-1]))
        else:
            return synxtaxfixer("\n".join(lines[:line_to_rm]))
        

#call prompt on openai model   
def call_prompt_on_model(
    prompt: str,  
    stop_w: str ,  
    max_tokens: int ,  
    code_model: str = "code-cushman-001",  
    temperature: float = 0.8,  
    reruns_if_empty: int = 2,  
    reruns_no_assert: int = 2, 
) -> str:
    
    
    explanation_response = openai.Completion.create(
    model=code_model,
    prompt=prompt,
    stop=stop_w,
    max_tokens=max_tokens,
    temperature=temperature,
    stream=True,
    )

    explanation_completion = ""
    for event in explanation_response:
        event_text = event["choices"][0]["text"]
        explanation_completion += event_text

    if reruns_if_empty>0 and all(elem == '\n' for elem in explanation_completion):
        print("empty output")
        return call_prompt_on_model(
            prompt = prompt,  
            stop_w = stop_w ,  
            code_model = code_model,  
            max_tokens = max_tokens,  
            temperature = temperature,  
            reruns_if_empty= reruns_if_empty-1, 
            reruns_no_assert = reruns_no_assert,
        )
    
    if reruns_no_assert>0 and not re.search('assert', explanation_completion):
        print("no assert in output")
        return call_prompt_on_model(
            prompt = prompt,  
            stop_w = stop_w ,  
            code_model = code_model,  
            max_tokens = max_tokens,  
            temperature = temperature,  
            reruns_if_empty= reruns_if_empty, 
            reruns_no_assert = reruns_no_assert-1,
        )
    
    

    return explanation_completion



#call the model on a specific prompt and return the output
def call_LLMs(initial_prompt,stop_w ,max_tokens):
    output = call_prompt_on_model(initial_prompt, stop_w, max_tokens)
    
    model_output = output
    
    print(initial_prompt)
    print("############")
    print(output)
    print("############")

    
    return model_output


#read the script from the file, generate the prompt, call the model on prompt and save the output of the model in another file
def generate_test_oracle_from_intial_file(fewshot_path, input_path):



    with open(input_path) as input:
        function_to_test = input.read()

    if fewshot_path:
        with open(fewshot_path) as fewshot:
            fewshot_content = fewshot.read()
        initial_prompt = fewshotPromptGenerator(fewshot_content,function_to_test)
    else:
        initial_prompt = initalPromptGenerator(function_to_test)

    model_output = call_LLMs(initial_prompt, "#</test>", 200) 
    
    print("inside function")
    print(model_output)
    print("############")

    file_content = function_to_test+ "\ndef test():\n" + model_output

    return(file_content)
    

#create the paths and call the function to generate the intial test oracle
def generate_test_oracle_intial(prmpt, DATASET, SCRIPT, name_string, output_string):
    CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Testing_" + DATASET,
                "",
            )

    SCRIPT_NAME =  name_string + SCRIPT + ".py"
    SCRIPT_PATH = os.path.join(CODE_DIR, SCRIPT, SCRIPT_NAME)

    os.makedirs(
        os.path.join(CODE_DIR, SCRIPT, "Codex"),
        exist_ok=True,
    )

    OUTPUT_NAME =  output_string + SCRIPT + ".py"
    OUTPUT_PATH = os.path.join(CODE_DIR, SCRIPT, "Codex", OUTPUT_NAME)

    if prmpt == "fewshot":
        FEWSHOT_DIR = os.path.join(CODE_DIR, "few_shot_query.py")
        file_content= generate_test_oracle_from_intial_file(FEWSHOT_DIR,SCRIPT_PATH)

    else:
        file_content= generate_test_oracle_from_intial_file(None,SCRIPT_PATH)

    with open(OUTPUT_PATH, "w") as output:
        output.write(file_content)
    output.close()

    return (OUTPUT_NAME +"\n")

#create the patth for studentEval dataset and call the function to generate the intial test oracle
def generate_test_oracle_student(prmpt, DATASET, SCRIPT, name_string, output_string):
    CODE_DIR = os.path.join(
                os.getcwd(),
                DATASET,
                "Reference_Scripts", "Tests",
                "",
            )

    SCRIPT_NAME =  name_string + SCRIPT + ".py"
    SCRIPT_PATH = os.path.join(CODE_DIR, SCRIPT, SCRIPT_NAME)

    os.makedirs(
        os.path.join(CODE_DIR,"Codex"),
        exist_ok=True,
    )

    OUTPUT_NAME =  output_string + SCRIPT + ".py"
    OUTPUT_PATH = os.path.join(CODE_DIR, SCRIPT, "Codex", OUTPUT_NAME)

    if prmpt == "fewshot":
        FEWSHOT_DIR = os.path.join(CODE_DIR, "few_shot_query.py")
        file_content= generate_test_oracle_from_intial_file(FEWSHOT_DIR,SCRIPT_PATH)

    else:
        file_content= generate_test_oracle_from_intial_file(None,SCRIPT_PATH)

    with open(OUTPUT_PATH, "w") as output:
        output.write(file_content)
    output.close()

    return (OUTPUT_NAME +"\n")



#read the intial test case from the file, call the model to fix the syntax error and save the fixed test case in another file
def check_test_oracle_synx(function_to_correct, rep):
    
    synx_LLMs= 0
    synx_split= 0
    
    syn_prompt = synxPromptGenerator(function_to_correct)

    while synxtaxCheck(function_to_correct) and rep>0:
        synx_LLMs = 1
        print("syntax error:", rep) 
        model_output = call_LLMs(syn_prompt,"#</test>",20)
        function_to_correct = function_to_correct + model_output.lstrip()
        rep-=1
     
      
    if synxtaxCheck(function_to_correct):
        synx_split= 1
        function_to_correct = synxtaxfixer(function_to_correct)


    return function_to_correct, synx_LLMs, synx_split


def apply_syntax_fix (DATASET, SCRIPT, name_string, output_string, csv_name):
    if DATASET == "StudentEval":
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
    
    script_name =  name_string + SCRIPT + ".py"
    input_path = os.path.join(CODE_DIR,  SCRIPT, "Codex", script_name)

    output_name =  output_string + SCRIPT + ".py"
    output_path = os.path.join(CODE_DIR,  SCRIPT, "Codex", output_name)

    csv_path = os.path.join(CODE_DIR, csv_name)


    with open(input_path) as input:
        function_to_correct = input.read()

    correct_function, synx_LLMs, synx_split = check_test_oracle_synx(function_to_correct, 3)

    file_name = input_path.split("/")[-1]

    print(output_name)

    with open(output_path, "w") as output:
        output.write(correct_function)
    output.close()

    with open(csv_path,'a') as csv_file:
        csv_file.write(file_name + "," + str(synx_LLMs) + "," + str(synx_split))
        csv_file.write("\n")

    return("done")

#141
#for till 100
#generate_test_oracle_intial("HumanEval", str(154), "script_NDS_", "test_oracle_NDS_")

#5, 14, 26, 28, 47, 53, 55, 57, 68, 85, 88, 89, 90, 95, 97, 101, 114, 117, 128, 135
#generate_test_oracle_intial("normal","HumanEval", str(163), "script_NDS_", "test_oracle_FS_")
#for till
#apply_syntax_fix("HumanEval", str(85), "test_oracle_NDS_", "T_O_NDS_synxfixed_", "normal_synx_fix.csv")

#apply_syntax_fix("HumanEval", str(163), "test_oracle_FS_", "T_O_FS_synxfixed_", "fewshot_synx_fix.csv")

#generate_test_oracle_student("StudentEval", "q"+str(1), "script_", "test_oracle_NDS_")

#generate_test_oracle_student("fewshot","StudentEval", "q"+str(5), "script_", "test_oracle_FS_")
#apply_syntax_fix("StudentEval", "q"+str(5), "test_oracle_NDS_", "T_O_NDS_synxfixed_", "normal_synx_fix.csv")

#92









