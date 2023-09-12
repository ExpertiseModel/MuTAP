
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
    # Test with an empty input string
    assert sort_numbers('') == '', "The result should be empty"

    # Test with a single digit string
    assert sort_numbers('5') == 'five', "The result should be 'five'"


    # Test with a multi-digit string
    assert sort_numbers('123') == 'one two three', "The result should be 'one two three'"

    # Test with a string that starts with zeros