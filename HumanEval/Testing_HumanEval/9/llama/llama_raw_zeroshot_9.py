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
    assert [/INST]  Certainly! Here are some test cases for the `rolling_max` function in Python:
```python
def test_single_ element_list():
    numbers = [1]
    result = rolling_max(numbers)
    assert result == [1]

def test_empty_list():
    numbers = []
    result = rolling_max(numbers)
    assert result == []

def test_list_of_ints():
    numbers = [1, 2, 3, 4, 5]
    result = rolling_max(numbers)
    assert result == [4, 5]

def test_list_of_floats():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = rolling_max(numbers)
    assert result == [4.0, 5.0]

def test_list_of_negatives():
    numbers = [-1, -2, -3, -4, -5]
    result = rolling_max(numbers)
    assert result == [-4,