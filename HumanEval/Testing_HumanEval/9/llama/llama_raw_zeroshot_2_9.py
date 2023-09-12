[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result




# test case
def test():
    assert [/INST]  Certainly! Here are some test cases for the `rolling_max` function using Python:
```
def test_empty_list():
    numbers = [ ]
    result = rolling_max(numbers)
    assert result == [0]

def test_single_number():
    numbers = [1]
    result = rolling_max(numbers)
    assert result == [1]

def test_small_list():
    numbers = [1, 2, 3, 4, 5]
    result = rolling_max(numbers)
    assert result == [4]

def test_large_list():
    numbers = range(10)
    result = rolling_max(numbers)
    assert result == [6]

def test_mixed_types():
    numbers = [1, 2, 3, 4, 5, 'hello']
    result = rolling_max(numbers)
    assert result == [4]

def test_negative_values():
    numbers = [-2, -1, 0, 1, 2]
    result = rolling_max