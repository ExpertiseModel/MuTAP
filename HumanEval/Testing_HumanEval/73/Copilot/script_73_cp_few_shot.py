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
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.
    """
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans

#</code>
#<test>

def test_smallest_change():
    assert smallest_change([1, 2, 3, 4, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert smallest_change([1, 2, 3, 4, 3, 2, 3]) == 2
    assert smallest_change([1, 2, 3, 4, 3, 2, 4]) == 3
    assert smallest_change([1, 2, 3, 4, 3, 2, 5]) == 4
    assert smallest_change([1, 2, 3, 4, 3, 2, 6]) == 5
    assert smallest_change([1, 2, 3, 4, 3, 2, 7]) == 6
    assert smallest_change([1, 2, 3, 4, 3, 2, 8]) == 7
    assert smallest_change([1, 2, 3, 4, 3, 2, 9]) == 8
    assert smallest_change([1, 2, 3, 4, 3, 2, 10]) == 9
    assert smallest_change([1, 2, 3, 4, 3, 2, 11]) == 10
    assert smallest_change([1, 2, 3, 4, 3, 2, 12]) == 11
    assert smallest_change([1, 2, 3, 4, 3, 2, 13]) == 12
    assert smallest_change([1, 2, 3, 4, 3, 2, 14]) == 13
    assert smallest_change([1, 2, 3, 4, 3, 2, 15]) == 14
    assert smallest_change([1, 2, 3, 4, 3, 2, 16]) == 15
    assert smallest_change([1, 2, 3, 4, 3, 2, 17]) == 16


