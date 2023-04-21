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
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    """
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])


METADATA = {}

#</code>
#<test>

def test_remove_vowels():
    assert remove_vowels("a") == ""
    assert remove_vowels("b") == "b"
    assert remove_vowels("aeiou") == ""
    assert remove_vowels("aeiouAEIOU") == ""
    assert remove_vowels("Hello") == "Hll"
    assert remove_vowels("Hello World") == "Hll Wrld"
    assert remove_vowels("U") == ""
    assert remove_vowels("u") == ""
    assert remove_vowels("AEIOU") == ""
    assert remove_vowels("aeiou") == ""
    assert remove_vowels("AEIOUaeiou") == ""
    assert remove_vowels("aeiouAEIOU") == ""
    assert remove_vowels("f") == "f"
    assert remove_vowels("g") == "g"
    assert remove_vowels("h") == "h"
    assert remove_vowels("j") == "j"
    assert remove_vowels("k") == "k"
