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
    assert [/INST]  Certainly! Here are some test cases for the `remove_duplicates` function in Python:
```python
def test_empty_list():
    assert remove_duplicates([]) == []

def test_single_element():
    assert remove_duplicates([1]) == [1]

def test_multiple_elements():
    assert remove_duplicates([1, 1, 2, 2, 3, 3]) == [1, 2, 3]

def test_duplicate_elements():
    assert remove_duplicates([1, 1, 2, 2, 3, 3, 3]) == [1, 2, 3]

def test_large_list():
    assert remove_duplicates([1, 2, 2, 3, 3, 3, 3, 4]) == [1, 2, 3, 4]

def test_mixed_types():
    assert remove_duplicates([1, 2, 'hello', 3, 3.0, True]) == [1, 2, 