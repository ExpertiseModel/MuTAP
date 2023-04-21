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
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]

#</code>
#<test>

def test_circular_shift():
    assert circular_shift(123, 1) == "312"
    assert circular_shift(123, 2) == "231"
    assert circular_shift(123, 3) == "123"
    assert circular_shift(123, 4) == "321"
    assert circular_shift(123, 5) == "123"
    assert circular_shift(123, 6) == "312"
    assert circular_shift(123, 7) == "231"
    assert circular_shift(123, 8) == "123"
    assert circular_shift(123, 9) == "321"
    assert circular_shift(123, 10) == "123"
    assert circular_shift(123, 11) == "312"
    assert circular_shift(123, 12) == "231"
    assert circular_shift(123, 13) == "123"
    assert circular_shift(123, 14) == "321"
    assert circular_shift(123, 15) == "123"
    assert circular_shift(123, 16) == "312"
    


