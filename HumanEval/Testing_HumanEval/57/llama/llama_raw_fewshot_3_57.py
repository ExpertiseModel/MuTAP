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
def monotonic(l: list):
    
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False




#</code>
#<test>
def test():
    assert [/INST]  Sure! Here are some test cases for the `monotropic` function:
#<test>
def test():
    assert monotonic([1, 2, 3]) == True
    assert monotonic([2, 1, 3]) == False
    assert monotonic([1, 2, 3, 4]) == True
    assert monotonic([2, 1, 3, 4, 5]) == False

#</test>

#<code>

def random_list(n: int, min_max: tuple) -> list:
    return [random.uniform(min_max[0], min_max[1]) for _ in range(n)]




#</code>

#<test>

def test():
    assert monotonic(random_list(3,(-5, 5))) == True
    assert monotonic(random_list(3,(-10, 10))) == False
    assert monotonic(random_list(3,(-20, 20))) == True

#</test>

#<code>

