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
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False


METADATA = {}



#</code>
#<test>


def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([0, 0]) == True
    assert pairs_sum_to_zero([0]) == False
    assert pairs_sum_to_zero([]) == False
    assert pairs_sum_to_zero([1, 2, 3, 4]) == False
    assert pairs_sum_to_zero([1, 2, 3, -2]) == True
    assert pairs_sum_to_zero([1, 2, 3, -3]) == True
    assert pairs_sum_to_zero([1, 2, 3, -1]) == True
    assert pairs_sum_to_zero([1, 2, 3, 0]) == False
    assert pairs_sum_to_zero([1, 2, 3, -4]) == False
    assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -4]) == False
    assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -4, -8]) == True





