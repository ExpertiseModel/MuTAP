from typing import List
from typing import List
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
def test_equilateral_triangle():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
#</test>
#<code>
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
def check(candidate):
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
#</test>
#<code>
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    """
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))

#</code>
#<test>

#wait here to collect unit tests

def test_sort_array():
    assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 4, 8, 3, 5, 6, 9, 10, 7]
    assert sort_array([2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 4, 8, 3, 5, 6, 9, 10, 7]
    assert sort_array([2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 8, 3, 5, 6, 9, 7]
    assert sort_array([2, 3, 4, 5, 6, 7, 8]) == [2, 4, 8, 3, 5, 6, 7]
    assert sort_array([2, 3, 4, 5, 6, 7]) == [2, 4, 3, 5, 6, 7]
    assert sort_array([2, 3, 4, 5, 6]) == [2, 4, 3, 5, 6]
    assert sort_array([2, 3, 4, 5]) == [2, 4, 3, 5]
    assert sort_array([2, 3, 4]) == [2, 4, 3]
    assert sort_array([2, 3]) == [2, 3]
    assert sort_array([2]) == [2]
    assert sort_array([3]) == [3]
    assert sort_array([]) == []


