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


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]



#</code>
#<test>

def test_rescale_to_unit():
    assert rescale_to_unit([0.0, 1.0]) == [0.0, 1.0]
    assert rescale_to_unit([0.0, 2.0]) == [0.0, 1.0]
    assert rescale_to_unit([0.0, 0.0]) == [0.0, 0.0]
    assert rescale_to_unit([0.0, 0.0, 1.0]) == [0.0, 0.0, 1.0]
    assert rescale_to_unit([0.0, 1.0, 2.0]) == [0.0, 0.5, 1.0]
    assert rescale_to_unit([0.0, 1.0, 2.0, 3.0]) == [0.0, 0.3333333333333333, 0.6666666666666666, 1.0]
    assert rescale_to_unit([3.0, 2.0, 1.0, 0.0]) == [1.0, 0.6666666666666666, 0.3333333333333333, 0.0]
    assert rescale_to_unit([1, 2, 3, 4, 5]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([1, 2, 3, 4, 5, 6]) == [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    assert rescale_to_unit([1, 2, 3, 4, 5, 6, 7]) == [0.0, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334, 1.0]
    assert rescale_to_unit([1, 2, 3, 4, 5, 6, 7, 8]) == [0.0, 0.14285714285714285, 0.2857142857142857, 0.42857142857142855, 0.5714285714285714, 0.7142857142857143, 0.8571428571428571, 1.0]
    assert rescale_to_unit([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0 ]

