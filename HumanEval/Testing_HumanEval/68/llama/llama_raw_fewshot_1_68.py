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



def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]


#</original code>

generate test in the form of above example tests for the original code:

#<test>
def test():
    assert [/INST]  Sure, I'd be happy to help you with that! Here's the original code in Python:
```
def pluck(arr):
    if (len(arr) == 0):
        return []
    evens = list(filter(lambda x: x % 2 == 0, arr))
    if (evens == []):
        return []
    return [min(evens), arr.index(min(evens))]
```
And here are some test cases for the `pluck` function:
```
def test():
    assert pluck([1, 2, 3, 4, 5]) == [2, 2]
    assert pluck([2, 4, 6, 8, 10]) == [4, 3]
    assert pluck([3, 5, 7, 9, 11]) == [7, 4]
    assert pluck([1, 2, 3, 4, 5]) == [1, 0]
    assert pluck([1, 2, 3, 4, 5]) == [