[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]




# test case
def test():
    assert [/INST]  Great! Here are some test cases for the `remove_duplicates` function:

test_cases = [
    ({expected: [1, 2, 3, 3], actual: [1, 2, 3, 3]},),
    ({expected: [1, 2, 3, 4], actual: [1, 2, 3]},),
    ({expected: [1, 2, 3, 4, 5], actual: [1, 2, 3, 4]},),
    ({expected: [1, 2, 3, 4, 5, 5], actual: [1, 2, 3]},),
    ({expected: [1, 2, 3, 4, 5, 6], actual: []},),
]
# Explain what each test case is testing
test_case 1: This test case is testing that the function removes duplicates from a list of integers. The expected output is `[1, 2, 3, 3]`. The actual output is correct.
test_case 2: This test case is