[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List


def sort_numbers(numbers: str) -> str:
    
    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return ' '.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))




# test case
def test():
    assert [/INST]  Sure, I'd be happy to help you generate test cases for the `sort_numbers` function! Here are some test cases you can use:
```python
def test_empty_input():
    # Test with an empty input string
    result = sort_numbers('')
    # Assert the result is empty
    assert result == '', "The result should be empty"

def test_single_digit_string():
    # Test with a single digit string
    result = sort_numbers('5')
    # Assert the result is the correct value
    assert result == 'five', "The result should be 'five'"

def test_multi_digit_string():
    # Test with a multi-digit string
    result = sort_numbers('123')
    # Assert the result is the correct value
    assert result == 'one two three', "The result should be 'one two three'"

def test_leading_zeros():
    # Test with a string that starts with zeros
    result = sort_numbers('0123')
    # Assert the result is the correct value
    assert result == 'one two three', "