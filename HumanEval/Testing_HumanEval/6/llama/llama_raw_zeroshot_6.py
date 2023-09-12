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
    assert [/INST]  Here are some test cases for the `parse_nested_parens` function using Python unit testing:
```python
import unittest

class TestNestedParens(unittest.TestCase):
    def test_empty_string(self):
        paren_string = ''
        result = parse_nested_parens(paren_string)
        self.assertEqual(result, [])
    def test_single_parenthesis(self):
        paren_string = '(a)'
        result = parse_nested_parens(paren_string)
        self.assertEqual(result, [1])
    def test_single_level(self):
        paren_string = '(a (b))'
        result = parse_nested_parens(paren_string)
        self.assertEqual(result, [1, 2])
    def test_multiple_levels(self):
        paren_string = '(a (b (c)))'
        result = parse_nested_parens(paren_string)
        self.assertEqual(result, [1, 2