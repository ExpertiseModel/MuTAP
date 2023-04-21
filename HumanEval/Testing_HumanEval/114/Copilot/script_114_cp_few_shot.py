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
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    """
    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if (s < 0):
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum = -max_sum
    return min_sum

#</code>
#<test>

#wait here to collect unit tests

def test_minSubArraySum():
    assert minSubArraySum([1, -1, 1]) == 1
    assert minSubArraySum([1, -2, 3]) == 2
    assert minSubArraySum([1, -2, 3, 10, -4, 7, 2, -5]) == 2
    assert minSubArraySum([-1, -1, -1, -1]) == 4
    assert minSubArraySum([-2, -3, -1]) == 6
    assert minSubArraySum([1, 2, 3]) == 1
    assert minSubArraySum([-1, -2, -3]) == 6
    assert minSubArraySum([1, 2, 3, -2, 5]) == 1
    assert minSubArraySum([1, 2, 3, -2, 5, -3]) == 1
    assert minSubArraySum([1, 2, 3, -2, 5, -3, 2]) == 1
    assert minSubArraySum([1, 2, 3, -2, 5, -3, 2, -1]) == 1
    assert minSubArraySum([1, 2, 3, -2, 5, -3, 2, -1, 2]) == 1
    assert minSubArraySum([1, 2, 3, -2, 5, -3, 2, -1, 2, 3]) == 1
    assert minSubArraySum([1, 2, 3, -2, 5, -3, 2, -1, 2, 3, -2]) == 1
    assert minSubArraySum([1, 2, 3, -2, 5, -3, 2, -1, 2, 3, -2, 3]) == 1
    assert minSubArraySum([1, 2, 3, -2, 5, -3, 2, -1, 2, 3, -2, 3, -1]) == 1


