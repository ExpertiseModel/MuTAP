[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def is_nested(string):
   
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        if string[i] == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2

    


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `is_ nested` function in Python:
```python
def test_is_nested_ Basic():
    input_strings = [
        "[]",
        "[ABC]",
        "][",
        "]",
        "]["
    ]
    for input_string in input_strings:
        output_value = is_nested(input_string)
        assert output_value == 1, f"Expected {input_string} to be nested, but got {output_value}"

def test_is_nested_ Empty():
    input_strings = [
        "",
        " ",
        " null",
        "undefined"
    ]
    for input_string in input_strings:
        output_value = is_nested(input_string)
        assert output_value == 0, f"Expected {input_string} to be non-nested, but got {output_value}"

def test_is_nested_ Single():
    input_strings = [
        "[ABC]"
        "[ABC][",
        "]["
    ]