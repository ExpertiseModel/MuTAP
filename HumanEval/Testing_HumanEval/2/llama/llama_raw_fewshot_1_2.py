[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 These are two examples of codes and their tests.

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
#</test>

#<original code>



def truncate_number(number: float) -> float:
    
    return number % 1.0




#</original code>

generate test in the form of above example tests for the original code:

#<test>
def test():
    assert [/INST]  Sure, I'd be happy to help! Here are the tests for the original code in the form of example tests:
#<test>


def test():
    assert truncate_number(1.0) == 1.0
    assert truncate_number(1.5) == 1.0
    assert truncate_number(2.0) == 2.0
    assert truncate_number(2.5) == 2.0
    assert truncate_number(3.0) == 3.0
    assert truncate_number(3.5) == 3.0
    assert truncate_number(4.0) == 4.0
    assert truncate_number(4.5) == 4.0
    assert truncate_number(5.0) == 5.0
    assert truncate_number(5.5) == 5.0
    assert truncate_number(6.0) == 6.0
    assert truncate_number(6.5) == 6.0
    assert truncate_number(7.0) == 7