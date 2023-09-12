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
def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

#</code>
#<test>
def test():
    assert [/INST]  Certainly! Here are some test cases for the `digitSum` function:
#<test>
def test_empty_input():
    assert digitSum("") == 0

def test_single_digit():
    assert digitSum("1") == 1

def test_multi_digits():
    assert digitSum("123") == 6

def test_uppercase_digits():
    assert digitSum("Go123") == 6

def test_mixed_case():
    assert digitSum("Go123") == 6

#</test>

Here are some test cases to test the `digitSum` function:
1. An empty input should return 0.
2. A single digit should return the digit's value.
3. Multiple digits separated by spaces should return the sum of their values.
4. Uppercase digits should be counted as well.
5. Mixed case digits should be counted as well.

Do you have any specific questions or concerns about these test cases?