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
def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    """
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret


METADATA = {}



#</code>
#<test>


def test_modp():
    assert modp(0, 2) == 1
    assert modp(1, 2) == 0
    assert modp(2, 2) == 0
    assert modp(3, 2) == 0
    assert modp(4, 2) == 0
    assert modp(5, 2) == 0
    assert modp(0, 5) == 1
    assert modp(1, 5) == 5
    assert modp(2, 5) == 4
    assert modp(3, 5) == 3
    assert modp(4, 5) == 1
    assert modp(5, 5) == 2
    assert modp(12, 3) == 1
    assert modp(13, 3) == 2
    assert modp(14, 3) == 1
    assert modp(15, 3) == 2


