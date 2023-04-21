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
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    """
    return "db" + bin(decimal)[2:] + "db"

#</code>
#<test>

def test_decimal_to_binary():
    assert decimal_to_binary(0) == "db0db"
    assert decimal_to_binary(1) == "db1db"
    assert decimal_to_binary(2) == "db10db"
    assert decimal_to_binary(3) == "db11db"
    assert decimal_to_binary(4) == "db100db"
    assert decimal_to_binary(5) == "db101db"
    assert decimal_to_binary(6) == "db110db"
    assert decimal_to_binary(7) == "db111db"
    assert decimal_to_binary(8) == "db1000db"
    assert decimal_to_binary(9) == "db1001db"
    assert decimal_to_binary(10) == "db1010db"
    assert decimal_to_binary(11) == "db1011db"
    assert decimal_to_binary(12) == "db1100db"
    assert decimal_to_binary(13) == "db1101db"
    assert decimal_to_binary(14) == "db1110db"
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(16) == "db10000db"
    assert decimal_to_binary(17) == "db10001db"
    assert decimal_to_binary(18) == "db10010db"
    