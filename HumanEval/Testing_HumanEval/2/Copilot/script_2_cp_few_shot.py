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
def truncate_number(number: float) -> float:
    
    return number % 1.0


#</code>
#<test>

def test_truncate_number():
    assert truncate_number(1.0) == 0.0
    assert truncate_number(1.1) == 0.1
    assert truncate_number(1.2) == 0.2
    assert truncate_number(1.3) == 0.3
    assert truncate_number(1.4) == 0.4
    assert truncate_number(1.5) == 0.5
    assert truncate_number(1.6) == 0.6
    assert truncate_number(1.7) == 0.7
    assert truncate_number(1.8) == 0.8
    assert truncate_number(1.9) == 0.9
    assert truncate_number(1.99) == 0.99
    assert truncate_number(1.999) == 0.999
    assert truncate_number(1.9999) == 0.9999
    assert truncate_number(1.99999) == 0.99999
    assert truncate_number(1.999999) == 0.999999
    assert truncate_number(1.9999999) == 0.9999999
    assert truncate_number(1.99999999) == 0.99999999
    assert truncate_number(1.999999999) == 0.999999999
    assert truncate_number(1.9999999999) == 0.9999999999
    assert truncate_number(1.99999999999) == 0.99999999999
    assert truncate_number(1.999999999999) == 0.999999999999
    assert truncate_number(1.9999999999999) == 0.9999999999999
    assert truncate_number(1.99999999999999) == 0.99999999999999
    assert truncate_number(1.999999999999999) == 0.999999999999999


