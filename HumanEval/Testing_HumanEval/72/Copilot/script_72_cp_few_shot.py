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
def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.
    '''
    if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while i<j:
        if q[i] != q[j]:
            return False
        i+=1
        j-=1
    return True

#</code>
#<test>

def test_will_it_fly():
    assert will_it_fly([1, 2, 3, 2, 1], 10) == True
    assert will_it_fly([1, 2, 3, 2, 1], 5) == False
    assert will_it_fly([1, 2, 3, 2, 1], 6) == True
    assert will_it_fly([1, 2, 3, 2, 1], 7) == True
    assert will_it_fly([1, 2, 3, 2, 1], 8) == True
    assert will_it_fly([1, 2, 3, 2, 1], 9) == True
    assert will_it_fly([1, 2, 3, 2, 1], 4) == False
    assert will_it_fly([1, 2, 3, 2, 1], 3) == False
    assert will_it_fly([1, 2, 3, 2, 1], 2) == False
    assert will_it_fly([1, 2, 3, 2, 1], 1) == False
    assert will_it_fly([1, 2, 3, 2, 1], 0) == False
    assert will_it_fly([1, 2, 3, 2, 1], -1) == False
    assert will_it_fly([1, 2, 3, 2, 1], -2) == False
    assert will_it_fly([1, 2, 3, 2, 1], -3) == False
    assert will_it_fly([1, 2, 3, 2, 1], -4) == False
    assert will_it_fly([1, 2, 3, 2, 1], -5) == False
    assert will_it_fly([1, 2, 3, 2, 1], -6) == False
    assert will_it_fly([1, 2, 3, 2, 1], -7) == False


