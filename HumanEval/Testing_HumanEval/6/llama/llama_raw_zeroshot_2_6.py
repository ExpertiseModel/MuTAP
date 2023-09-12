[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1

        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `parse_ nested Parens` function in Python:
```
def test_empty_paren_string():
    paren_string = ""
    result = parse_nested_parens(paren_string)
    assert result == []

def test_single_paren():
    paren_string = " ()"
    result = parse_nested_parens(paren_string)
    assert result == [1]

def test_multiple_parens():
    paren_string = ")()()()"
    result = parse_nested_parens(paren_string)
    assert result == [3]

def test_paren_group_deeper():
    paren_string = ")((((())"
    result = parse_nested_parens(paren_string)
    assert result == [4]

def test_mix_parens_and_spaces():
    paren_string = ") ( Hello World  ()"
    result = parse_nested_parens(paren_string)
    assert result == [2, 3