from typing import List
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
from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    """
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False



#</code>
#<test>

def test_below_zero():
    assert below_zero([1, 2, 3, -1, -2, -3]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3, -4]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3, -4, 1]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3, -4, 1, 2]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3, -4, 1, 2, 3]) == False

