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
def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    
    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])

#</code>
#<test>

#wait here to collect unit tests
def test_max_fill():
    assert max_fill([[1, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]], 1) == 5
    assert max_fill([[1, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]], 2) == 3
    assert max_fill([[1, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]], 3) == 2
    assert max_fill([[1, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]], 4) == 2
    assert max_fill([[1, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]], 5) == 1


