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
def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    """
    return sum(range(n + 1))


METADATA = {}



#</code>
#<test>

def test_sum_to_n():
    assert sum_to_n(0) == 0
    assert sum_to_n(1) == 1
    assert sum_to_n(2) == 3
    assert sum_to_n(3) == 6
    assert sum_to_n(4) == 10
    assert sum_to_n(5) == 15
    assert sum_to_n(6) == 21
    assert sum_to_n(7) == 28
    assert sum_to_n(8) == 36
    assert sum_to_n(9) == 45
    assert sum_to_n(10) == 55
    assert sum_to_n(11) == 66
    assert sum_to_n(12) == 78
    assert sum_to_n(13) == 91
    assert sum_to_n(14) == 105
    assert sum_to_n(15) == 120
    assert sum_to_n(16) == 136
    assert sum_to_n(17) == 153
    