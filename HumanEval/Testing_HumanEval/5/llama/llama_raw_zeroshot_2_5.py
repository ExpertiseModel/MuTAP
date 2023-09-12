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
    assert [/INST]  Here are some test cases for the `intersperse` function in Python:
```python
def test_single_number():
    assert intersperse([1], 0) == [1]

def test_empty_list():
    assert intersperse( [], 0) == []

def test_non_empty_list():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

def test_non_int_type():
    with pytest.raises(TypeError):
        intersperse(["a"], 0)

def test_neg_delimeter():
    assert intersperse([1, 2, 3], -1) == [1, 2, 0, 3]

def test_pos_delimeter():
    assert intersperse([1, 2, 3], 1) == [1, 0, 1, 0, 3]

def test_duplicate_numbers():
    assert intersperse([