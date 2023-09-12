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



def common(l1: list, l2: list):
    
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))




#</original code>

generate test in the form of above example tests for the original code:

#<test>
def test():
    assert [/INST]  Sure! Here's the code for the tests:
# Test 1
def test_common_empty_ lists():
    assert common([], []) == []
# Test 2
def test_common_single_element_lists():
    assert common([1], [1]) == [1]
# Test 3
def test_common_two_element_lists():
    assert common([1, 2], [2, 1]) == [1, 2]
# Test 4
def test_common_three_element_lists():
    assert common([1, 2, 3], [2, 3, 1]) == [1, 2, 3]
# Test 5
def test_common_same_elements_lists():
    assert common([1, 2, 2], [2, 2, 1]) == [1, 2, 2]
# Test 6
def test_common_different_elements_lists():
    assert common([1, 2, 3], [4, 5, 6]) == []







