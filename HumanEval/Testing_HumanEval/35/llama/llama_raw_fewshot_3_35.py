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
def max_element(l: list):
    
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m




#</code>
#<test>
def test():
    assert [/INST]  Here are some test cases for the `max_element` function:

#<test>

def test():

    # Test with a list ofnumbers
    assert max_element([1, 2, 3, 4, 5]) == 5
    # Test with a list of strings
    assert max_element(['a', 'b', 'c', 'd', 'e']) == 'e'
    # Test with a list of Complex numbers
    assert max_element([1 + 2j, 3 + 4j, 5 + 6j]) == 6j

#</test>

#<code>

def median(numbers: List[float]) -> float:
    if len(numbers) % 2 == 0:
        return (numbers[0] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]





#</code>


#<test>

def test():
    assert median([1, 2, 3, 4, 5]) ==