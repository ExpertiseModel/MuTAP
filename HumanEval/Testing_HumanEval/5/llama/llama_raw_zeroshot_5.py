[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result




# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `intersperse` function:
```python
def test_empty_list():
    numbers = []
    assert intersperse(numbers, 0) == []

def test_single_value():
    numbers = [1]
    assert intersperse(numbers, 0) == [1]

def test_multiple_values():
    numbers = [1, 2, 3]
    assert intersperse(numbers, 0) == [1, 0, 2, 0, 3]

def test_different_delimeter():
    numbers = [1, 2, 3]
    assert intersperse(numbers, 2) == [1, 2, 0, 2, 3]

def test_non_int_values():
    numbers = [1, "hello", 3.0]
    assert intersperse(numbers, 0) == [1, 0, "hello", 0, 3]

def test_empty_list_with_none():
