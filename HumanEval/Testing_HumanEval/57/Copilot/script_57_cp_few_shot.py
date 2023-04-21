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
    assert candidate([-1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.05) == True
    assert candidate([], 0.05) == True
#</test>
#<code>
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    """
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False


METADATA = {}



#</code>
#<test>

def test_monotonic():
    assert monotonic([1, 2, 3, 4, 5]) == True
    assert monotonic([5, 4, 3, 2, 1]) == True
    assert monotonic([1, 5, 2, 3, 4]) == False
    assert monotonic([1, 5, 2, 3, 4, 4]) == False
    assert monotonic([1, 2, 2, 3, 4]) == True
    assert monotonic([1, 2, 2, 3, 4, 4]) == True
    assert monotonic([1, 2, 2, 3, 4, 4, 5]) == False
    assert monotonic([1, 2, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8]) == False
    assert monotonic([1]) == True
    assert monotonic([]) == True


