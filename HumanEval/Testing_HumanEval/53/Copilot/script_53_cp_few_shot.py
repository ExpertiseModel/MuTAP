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
def add(x: int, y: int):
    """Add two numbers x and y
    """
    return x + y


METADATA = {}



#</code>
#<test>

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(-2, -3) == -5
     assert add(0, 0) == 0
    assert add(1, 2) == 3
    assert add(1, 3) == 4
    assert add(2, 2) == 4
    assert add(2, 3) == 5
    assert add(3, 3) == 6
    assert add(3, 4) == 7
    assert add(4, 4) == 8
    assert add(4, 5) == 9
    assert add(5, 5) == 10
    assert add(5, 6) == 11
    assert add(6, 6) == 12



