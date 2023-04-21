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
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    """
    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times



#</code>
#<test>


def test_how_many_times():
    assert how_many_times("abc", "a") == 1
    assert how_many_times("abc", "b") == 1
    assert how_many_times("abc", "c") == 1
    assert how_many_times("abc", "ab") == 1
    assert how_many_times("abc", "bc") == 1
    assert how_many_times("abc", "abc") == 1
    assert how_many_times("abc", "abcd") == 0
    assert how_many_times("abc", "bcde") == 0
    assert how_many_times("abc", "abcde") == 0
    assert how_many_times("abc", "aabc") == 1
    assert how_many_times("abc", "abbc") == 0
    assert how_many_times("abc", "abcc") == 0
    assert how_many_times("abc", "abccc") == 0
    assert how_many_times("abc", "abca") == 0
    assert how_many_times("abc", "abcb") == 0
    assert how_many_times("abc", "abcc") == 0
    assert how_many_times("abc", "abccc") == 0
    assert how_many_times("abc", "abca") == 0
    assert how_many_times("abc", "abcb") == 0
    assert how_many_times("abc", "abcc") == 0
    assert how_many_times("abc", "abccc") == 0
   

