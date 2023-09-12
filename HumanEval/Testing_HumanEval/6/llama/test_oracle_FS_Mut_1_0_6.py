[INST] <<SYS>>
#You are a python coding assistant. Always answer with python code.
<</SYS>>

#Generate test cases for the following function:```python
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






``` [/INST] ```python
 def test():
    
    assert parse_nested_parens("((((2+2)*3) + 4) * 5") == [4, 0, 0, 0, 0]
    assert parse_nested_parens("(4+5) * (6-3)") == [1, 0, 1]
    assert parse_nested_parens("(2*2) + 3 + (4-2) * (5+2)") == [1, 0, 0, 0, 1, 0, 1]
 ```  [INST] #The test cases that you generated in test() function, cannot detect the change in the following code snippet.
```python
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
                depth += 1

        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]



```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST] Sure! Here's a new test case that can detect the change in the code snippet you provided:
```python

def test():
    # Change in code
    paren_string = "(((2+2)*3) + 4) * (5-3)"
    # New test case
    assert parse_nested_parens(paren_string) == [4, 0, 0, 0, 1, 0, 1]
```
This test case will pass if the `parse_nested_parens` function can correctly handle the change in the code snippet, and fail otherwise.