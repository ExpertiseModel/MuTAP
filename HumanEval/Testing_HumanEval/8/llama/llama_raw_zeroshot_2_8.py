[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `sum_product` function:
```
def test_sum_value():
    numbers = [1, 2, 3, 4, 5]
    result, *_ = sum_product( numbers )
    assert result == 15

def test_prod_value():
    numbers = [2, 3, 4, 5, 6]
    result, *_ = sum_product( numbers )
    assert result == 120

def test_empty_list():
    numbers = [ ]
    result, *_ = sum_product( numbers )
    assert result == (0, 1)

def test_negative_values():
    numbers = [ -1, -2, -3, -4, -5]
    result, *_ = sum_product( numbers )
    assert result == (0, -120)

def test_non_int_values():
    numbers = [1, "hello", 4.5, -0.5]
    result, *_ = sum_product( numbers )
