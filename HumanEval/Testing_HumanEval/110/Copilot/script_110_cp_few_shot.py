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
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    """
    odd = 0
    even = 0
    for i in lst1:
        if i%2 == 1:
            odd += 1
    for i in lst2:
        if i%2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"
            

#</code>
#<test>

#wait here to collect unit tests

def test_exchange():
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert exchange([1, 2, 3, 4], [1, 2, 3, 5]) == "NO"
    assert exchange([1, 1, 1, 1], [1, 2, 3, 4]) == "YES"
    assert exchange([1, 1, 1, 1], [1, 2, 3, 5]) == "NO"
    assert exchange([1, 2, 3, 4], [1, 1, 1, 1]) == "YES"
    assert exchange([1, 2, 3, 5], [1, 1, 1, 1]) == "NO"
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4, 5]) == "YES"
    assert exchange([1, 2, 3, 5], [1, 2, 3, 4, 5]) == "NO"
    assert exchange([1, 2, 3, 4, 5], [1, 2, 3, 4]) == "YES"
    assert exchange([1, 2, 3, 4, 5], [1, 2, 3, 5]) == "NO"
    assert exchange([1, 1, 1, 1], [1, 2, 3, 4, 5]) == "YES"
    assert exchange([1, 1, 1, 1], [1, 2, 3, 5]) == "NO"
    assert exchange([1, 2, 3, 4, 5], [1, 1, 1, 1]) == "YES"
    assert exchange([1, 2, 3, 5], [1, 1, 1, 1]) == "NO"
    assert exchange([1, 2, 3, 4, 5], [1, 2, 3, 4]) == "YES"
    assert exchange([1, 2, 3, 4, 5], [1, 2, 3, 5]) == "NO"
