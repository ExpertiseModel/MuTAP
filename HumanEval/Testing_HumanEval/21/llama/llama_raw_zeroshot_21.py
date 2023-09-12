[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `rescale_to_unit` function:
```
def test_range_of_values():
    numbers = [1, 2, 3, 4, 5, 6]
    assert rescale_to_unit(numbers) == [0.2, 0.4, 0.6, 0.8, 1, 1.2]

def test_single_number():
    numbers = [1.5]
    assert rescale_to_unit(numbers) == [0.5]

def test_edge_cases():
    numbers = [-1, 0, 1]
    assert rescale_to_unit(numbers) == [-0.5, 0, 1]

def test_list_of_numbers():
    numbers = [2, 4, 6, 8, 10, 12]
    assert rescale_to_unit(numbers) == [0.4, 0.6, 0.8, 1, 1.2, 1.