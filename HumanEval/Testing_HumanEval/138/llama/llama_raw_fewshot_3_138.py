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
def is_equal_to_sum_even(n):
    
    return n%2 == 0 and n >= 8


#</code>
#<test>
def test():
    assert [/INST]  Sure! Here are some test cases for the `is_equal_to_sum_even` function:
Test Case 1:
* Input: n = 4
* Expected output: True
* Reason: 4%2 == 0 and 4 >= 8

Test Case 2:
* Input: n = 6
* Expected output: False
* Reason: 6%2 == 0 and 6 >= 8

Test Case 3:
* Input: n = 3
* Expected output: False
* Reason: 3%2 == 0 and 3 >= 8

Test Case 4:
* Input: n = 10
* Expected output: True
* Reason: 10%2 == 0 and 10 >= 8

Test Case 5:
* Input: n = -4
* Expected output: False
* Reason: (-4)%2 == 0 and (-4) >= 8

Test Case 6:
* Input: n = 12
* Expected output: True
* Reason: 