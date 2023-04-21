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
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.
    """
    res = []
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
    return res

#</code>
#<test>

#wait here to collect unit tests

def test_odd_count():
    assert odd_count(["123", "456", "789"]) == ["the number of odd elements 2 in the string 2 of the input.", "the number of odd elements 0 in the string 0 of the input.", "the number of odd elements 3 in the string 3 of the input."]
    assert odd_count(["11", "22", "33"]) == ["the number of odd elements 2 in the string 2 of the input.", "the number of odd elements 0 in the string 0 of the input.", "the number of odd elements 2 in the string 2 of the input."]
    assert odd_count(["1", "2", "3"]) == ["the number of odd elements 1 in the string 1 of the input.", "the number of odd elements 1 in the string 1 of the input.", "the number of odd elements 1 in the string 1 of the input."]
    assert odd_count(["0", "1", "2"]) == ["the number of odd elements 0 in the string 0 of the input.", "the number of odd elements 1 in the string 1 of the input.", "the number of odd elements 1 in the string 1 of the input."]
    assert odd_count(["00", "01", "02"]) == ["the number of odd elements 0 in the string 0 of the input.", "the number of odd elements 1 in the string 1 of the input.", "the number of odd elements 1 in the string 1 of the input."]
    assert odd_count(["000", "001", "002"]) == ["the number of odd elements 0 in the string 0 of the input.", "the number of odd elements 1 in the string 1 of the input.", "the number of odd elements 1 in the string 1 of the input."]



