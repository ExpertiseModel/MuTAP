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
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    '''
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2

#</code>
#<test>

def test_total_match():
    assert total_match(['a', 'b', 'c'], ['aa', 'bb', 'cc']) == ['a', 'b', 'c']
    assert total_match(['aa', 'bb', 'cc'], ['a', 'b', 'c']) == ['a', 'b', 'c']
    assert total_match(['aa', 'bb', 'cc'], ['aaa', 'bbb', 'ccc']) == ['aa', 'bb', 'cc']
    assert total_match(['aaa', 'bbb', 'ccc'], ['aa', 'bb', 'cc']) == ['aa', 'bb', 'cc']
    assert total_match(['aa', 'bb', 'cc'], ['aaa', 'bbb']) == ['aa', 'bb', 'cc']
    assert total_match(['aaa', 'bbb'], ['aa', 'bb', 'cc']) == ['aa', 'bb', 'cc']
    assert total_match(['aa', 'bb', 'cc'], ['aaa', 'bbb', 'ccc', 'dddd']) == ['aa', 'bb', 'cc']
    assert total_match(['aaa', 'bbb', 'ccc', 'dddd'], ['aa', 'bb', 'cc']) == ['aa', 'bb', 'cc']
    assert total_match(['aa', 'bb', 'cc'], ['aaa', 'bbb', 'ccc', 'dddd', 'eeeee']) == ['aa', 'bb', 'cc']
    assert total_match(['aaa', 'bbb', 'ccc', 'dddd', 'eeeee'], ['aa', 'bb', 'cc']) == ['aa', 'bb', 'cc']
    assert total_match(['aa', 'bb', 'cc'], ['aaa', 'bbb', 'ccc', 'dddd', 'eeeee', 'ffffff']) == ['aa', 'bb', 'cc']
    assert total_match(['aaa', 'bbb', 'ccc', 'dddd', 'eeeee', 'ffffff'], ['aa', 'bb', 'cc']) == ['aa', 'bb', 'cc']
    assert total_match(['aa', 'bb', 'cc'], ['aaa', 'bbb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg']) == ['aa', 'bb', 'cc']


