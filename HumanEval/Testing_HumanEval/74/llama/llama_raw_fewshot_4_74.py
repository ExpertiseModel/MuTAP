[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

Generate a test function that includes different tests in the form of one line assertion [/INST] These are examples of code and test case function:

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

def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
#</test>

#<code>

from typing import List
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

def test():
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
#</test>  [INST] Based on the examples of function code and their test function, generate test cases for the following function:
#<code>
def total_match(lst1, lst2):
   
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
def test():
    assert [/INST]  Sure, here are some test cases for the `total_match` function:

#<testCase>
def test_lst1_lst2_equal_length():
    lst1 = ['apple', 'banana', 'cherry']
    lst2 = ['banana', 'cherry', 'date']
    assert total_match(lst1, lst2) == lst1
#</testCase>

#<testCase>
def test_lst1_lst2_diff_length():
    lst1 = ['apple', 'banana', 'cherry']
    lst2 = ['banana', 'date', 'orange']
    assert total_match(lst1, lst2) == lst2
#</testCase>

#<testCase>
def test_lst1_lst2_partial_match():
    lst1 = ['apple', 'banana', 'cherry']
    lst2 = ['banana', 'date', 'orange']
    assert total_match(lst1, lst2) == ['banana']
#</testCase>

#<testCase>
def test_lst