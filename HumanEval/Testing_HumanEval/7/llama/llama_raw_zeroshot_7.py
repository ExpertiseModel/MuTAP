[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    
    return [x for x in strings if substring in x]




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `filter_by_substring` function in Python:

test('filter_by_substring', ['hello', 'world', 'abc'], 'abc')

# Test that the function returns a list of strings that contain the substring 'abc'
assert filter_by_substring(['hello', 'world', 'abc'], 'abc') == ['abc']

test('filter_by_substring', ['hello', 'world', 'abc'], 'abcdef')

# Test that the function ignores case
assert filter_by_substring(['hello', 'World', 'abc'], 'Abc') == ['abc']

test('filter_by_substring', ['hello', 'world', 'abc'], 'ABC')

# Test that the function works with multiple substrings
assert filter_by_substring(['hello', 'world', 'abc', 'def'], 'abc', 'def') == ['abc', 'def']

test('filter_by_substring', ['hello', 'world', 'abc', 'def'], 'a', 'd')

# Test that the function raises a ValueError if the input list is empty
assert