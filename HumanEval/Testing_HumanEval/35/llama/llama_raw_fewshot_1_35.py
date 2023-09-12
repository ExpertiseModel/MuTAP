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



def max_element(l: list):
    
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m




#</original code>

generate test in the form of above example tests for the original code:

#<test>
def test():
    assert [/INST]  Sure! Here is the code to test the `max_element` function:
```
#<code>

def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([1, 2, 3, 4]) == 4
    assert max_element([1, 2, 3, 4, 5]) == 5

#</code>

And here is the code to test the `has_close_elements` function:

```
#<code>

def test_has_close_elements():
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.5) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.1) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.