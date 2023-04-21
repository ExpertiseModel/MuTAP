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
def pluck(arr):
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].
    """
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]

#</code>
#<test>

def test_pluck():
    assert pluck([1, 2, 3, 4, 5]) == [2, 1]
    assert pluck([1, 3, 5, 7]) == []
    assert pluck([2, 4, 6, 8]) == [2, 0]
    assert pluck([2, 4, 6, 8, 10]) == [2, 0]
    assert pluck([1, 3, 5, 7, 9]) == []
    assert pluck([1, 3, 5, 7, 2]) == [2, 4]
    assert pluck([1, 3, 5, 7, 9, 11, 13, 14]) == [14, 7]
    assert pluck([1, 3, 5, 7, 9, 11, 13, 14, 2]) == [2, 8]
    assert pluck([1, 3, 5, 7, 9, 11, 13, 14, 2, 4]) == [2, 8]
    assert pluck([1, 3, 5, 7, 9, 11, 13, 14, 2, 4, 6]) == [2, 8]
    assert pluck([1, 3, 5, 7, 9, 11, 13, 14, 2, 4, 6, 8]) == [2, 8]
    assert pluck([1, 3, 5, 7, 9, 11, 13, 14, 2, 4, 6, 8, 10]) == [2, 8]
    assert pluck([1, 3, 5, 7, 9, 11, 13, 14, 2, 4, 6, 8, 10, 12]) == [2, 8]
    