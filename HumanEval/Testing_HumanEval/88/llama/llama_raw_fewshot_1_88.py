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



def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 


#</original code>

generate test in the form of above example tests for the original code:

#<test>
def test():
    assert [/INST]  Sure, here are the tests for the original code `sort_array`:
#<test>
def test():
    assert sort_array([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert sort_array([1, 2, 3, 4, 5, 6], reverse=True) == [6, 5, 4, 3, 2, 1]
    assert sort_array([1, 2, 3, 4, 5, 6], reverse=True) == [6, 5, 4, 3, 2, 1]
    assert sort_array([]) == []
    assert sort_array([]) == []
#</test>

Note that these tests are basic and do not cover all possible scenarios. You may want to come up with more complex test cases to ensure that the function works correctly in a wider range of situations.