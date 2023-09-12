[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `mean_absolute_deviation` function:
```
def test_empty_list():
    numbers = []
    result = mean_absolute_deviation(numbers)
    assert result == 0.0

def test_single_number():
    numbers = [1.0]
    result = mean_absolute_deviation(numbers)
    assert result == 1.0

def test_dupe_numbers():
    numbers = [1.0, 1.0, 2.0]
    result = mean_absolute_deviation(numbers)
    assert result == 1.5

def test_random_numbers():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = mean_absolute_deviation(numbers)
    assert result == 2.5

def test_negative_numbers():
    numbers = [-1.0, -2.0, -3.0, -4.0, -5.0]
    result = mean_absolute_deviation