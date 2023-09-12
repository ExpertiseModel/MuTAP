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
def truncate_number(number: float) -> float:
    
    return number % 1.0




#</code>
#<test>
def test():
    assert [/INST]  Here are some test cases for the `truncate_number` function:

#<test>
def test_truncate_number():
    assert truncate_number(0.1) == 0.1
    assert truncate_number(1.1) == 1.0
    assert truncate_number(-0.1) == -0.1
    assert truncate_number(2.3) == 2.0
    assert truncate_number(3.7) == 3.0
    assert truncate_number(-3.7) == -3.0
    assert truncate_number(4.5) == 4.0
    assert truncate_number(-4.5) == -4.0
#</test>








#<code>


def sum_of_digits(n: int) -> int:
    return sum(int(n % 10) for _ in range(10))





























