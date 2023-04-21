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
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    """
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value




#</code>
#<test>

def test_sum_product():
    assert sum_product([]) == (0, 1)
    assert sum_product([1]) == (1, 1)
    assert sum_product([1, 2]) == (3, 2)
    assert sum_product([1, 2, 3]) == (6, 6)
    assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([1, 2, 3, 4, 5]) == (15, 120)
    assert sum_product([1, 2, 3, 4, 5, 6]) == (21, 720)
    assert sum_product([1, 2, 3, 4, 5, 6, 7]) == (28, 5040)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8]) == (36, 40320)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9]) == (45, 362880)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (55, 3628800)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == (66, 39916800)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == (78, 479001600)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == (91, 6227020800)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == (105, 87178291200)
   


