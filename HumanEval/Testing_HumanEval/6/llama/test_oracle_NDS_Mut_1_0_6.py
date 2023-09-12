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




# test case

``` [/INST] ```python
 def test():
    
    #test_empty_string
    assert parse_nested_parens('') == []
    #test_single_parenthesis
    assert parse_nested_parens('(a)') == [1]
    #test_single_level(self):
    assert parse_nested_parens('(a (b))') == [1, 1]
    #test_multiple_levels(self):
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
    assert [/INST] Sure, here's a new test case that can detect the change in the code snippet you provided:
```python
def test():
    #test_modified_code
    # Change the code in the function to match the modified code
    assert parse_nested_parens('(a (b (c)))') == [1, 2, 3]
```
This test case will pass if the function returns the correct list of integers for the given input string, which has been modified to have a deeper nesting of parentheses.