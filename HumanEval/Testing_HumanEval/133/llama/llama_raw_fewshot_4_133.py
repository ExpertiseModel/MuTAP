[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

Generate a test function that includes different tests in the form of one line assertion [/INST] These are examples of code and test case function:

#<code> 

def triangle(x: int, y: int, z: int) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
#</code>

#<test>

def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
#</test>

#<code>

from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False
#</code>

#<test>

def test():
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
#</test>  [INST] Based on the examples of function code and their test function, generate test cases for the following function:
#<code>
def sum_squares(lst):
    
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared


#</code>
#<test>
def test():
    assert [/INST]  Sure! Here are some test cases for the `sum_squares` function:
#<test>
def test_empty_list():
    lst = []
    assert sum_squares(lst) == 0

#<test>

def test_single_value_list():
    lst = [3]
    assert sum_squares(lst) == 9

#<test>

def test_odd_values():
    lst = [3, 5, 7, 3]
    assert sum_squares(lst) == 51

#<test>

def test_even_values():
    lst = [4, 6, 8, 10]
    assert sum_squares(lst) == 320

#</test>

#<code>

def median_of_three(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3


def test_median_of_three():
    assert median_of_three(1.0, 2.