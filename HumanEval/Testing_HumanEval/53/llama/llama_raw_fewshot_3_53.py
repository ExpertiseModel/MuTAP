[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

Generate test cases. [/INST] These are examples of function code and test functions:

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
def add(x: int, y: int):
    
    return x + y




#</code>
#<test>
def test():
    assert [/INST]  Certainly! Here are some test cases for the `add` function:
#<test>

def test_negative_values():
    # Test with negative numbers
    assert add(-2, -3) == -5
    assert add(2, -3) == -1
    assert add(-2, 3) == 1
    assert add(2, 3) == 5
#</test>

#<test>

def test_zero_values():
    # Test with zero values
    assert add(0, 0) == 0
    assert add(0, -0) == 0
    assert add(0, 0) == 0
#</test>

#<test>

def test_large_values():
    # Test with large values
    assert add(1000, 1001) == 2002
    assert add(1000, -1001) == -1001
    assert add(1000, 0) == 1000
#</test>

#<test