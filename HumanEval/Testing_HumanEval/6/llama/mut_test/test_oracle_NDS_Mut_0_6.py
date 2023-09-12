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
 ```  [INST] #The test cases that you generated in test(), cannot detect the mutation in the following code snippet.
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
    assert [/INST]  ```python
def test():
    # test_mutation
    paren_string = '(a (b (c)))'
    # Create a mocked version of the function with the mutation
    def parse_nested_parens_mutated(paren_string: str) -> List[int]:
        return [parse_paren_group(x) for x in paren_string.split(' ') if x]

    # Call the mocked function with the original input
    assert parse_nested_parens_mutated(paren_string) == [1, 1, 1]
```

This new test case uses the `assert` statement to check that the mutated version of the function returns the correct output when given the original input. In this case, the input `paren_string` is `'(a (b (c)))'`, and the function returns ` [1, 1, 1]`. If the mutated function were to return a different output, the test would fail.