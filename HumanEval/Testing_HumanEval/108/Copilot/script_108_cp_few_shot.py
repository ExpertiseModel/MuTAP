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
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    """
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))

#</code>
#<test>

#wait here to collect unit tests
def test_count_nums():
    assert count_nums([1, 2, 3, 4, 5]) == 5
    assert count_nums([-1, 2, 3, 4, 5]) == 4
    assert count_nums([-1, -2, -3, -4, -5]) == 0
    assert count_nums([-1, -2, -3, -4, -5, 100]) == 1
    assert count_nums([1, 2, 3, 4, 5, -100]) == 5
    assert count_nums([1, 2, 3, 4, 5, -100, -1000, 1000]) == 6
    assert count_nums([-1, -2, -3, -4, -5, -100, -1000, -1000]) == 0
    assert count_nums([1, 2, 3, 4, 5, -100, -1000, -1000, 1000, 10000]) == 7
    assert count_nums([1, 2, 3, 4, 5, -100, -1000, -1000, 1000, 10000, -12345]) == 7
    assert count_nums([1, 2, 3, 4, 5, -100, -1000, -1000, 1000, 10000, -12345, 12345]) == 8

