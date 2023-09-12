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
    assert [/INST]  Of course! Here are some test cases for the `rescale_to_unit` function:
```
def test_rescale_to_unit():
    # Test with a list of numbers that are all the same
    numbers = [1, 1, 1, 1, 1]
    assert rescale_to_unit(numbers) == [0.5, 0.5, 0.5, 0.5, 0.5]
    # Test with a list of numbers that are all different
    numbers = [3.14, -2.7, 0.001, 10, -100]
    assert rescale_to_unit(numbers) == [0.32, -0.35, 0.0003, 1, -10]
    # Test with a list of numbers that contain both positive and negative values
    numbers = [2, -3, 4, -5, 6]
    assert rescale_to_unit(numbers) == [0.67, -0.43, 0