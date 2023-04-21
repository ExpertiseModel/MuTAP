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
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    begin, end = -1., 1.
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return begin


METADATA = {}



#</code>
#<test>

def test_find_zero():
    assert find_zero([1, 0, -1]) == 1
    assert find_zero([1, 0, -4]) == 2
    assert find_zero([1, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, -8]) == 2
    assert find_zero([1, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, -16]) == 2
    assert find_zero([1, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, -32]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, 0, -64]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, 0, 0, -128]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, -256]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, 0, -512]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 1

