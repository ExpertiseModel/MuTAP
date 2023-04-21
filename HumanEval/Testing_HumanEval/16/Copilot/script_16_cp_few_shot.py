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
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    """
    return len(set(string.lower()))





#</code>
#<test>

def test_count_distinct_characters():
    assert count_distinct_characters("") == 0
    assert count_distinct_characters("a") == 1
    assert count_distinct_characters("aa") == 1
    assert count_distinct_characters("ab") == 2
    assert count_distinct_characters("aba") == 2
    assert count_distinct_characters("Aba") == 2
    assert count_distinct_characters("AbaB") == 3
    assert count_distinct_characters("AbaBa") == 3
    assert count_distinct_characters("AbaBaB") == 3
    assert count_distinct_characters("AbaBaBb") == 4
    assert count_distinct_characters("AbaBaBbB") == 4
    assert count_distinct_characters("AbaBaBbBa") == 4
    assert count_distinct_characters("AbaBaBbBaB") == 4
    assert count_distinct_characters("aA") == 1
    assert count_distinct_characters("aAbB") == 2
    assert count_distinct_characters("aAbBcCdD") == 4
    assert count_distinct_characters("aAbBcCdD123") == 6
    assert count_distinct_characters("aAbBcCdD123!@#") == 9
    assert count_distinct_characters("aAbBcCdD123!@#_") == 10

