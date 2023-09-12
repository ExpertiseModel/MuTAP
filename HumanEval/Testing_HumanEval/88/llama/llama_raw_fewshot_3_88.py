[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

Generate test cases. [/INST] These are examples of function code and test functions:

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
def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 


#</code>
#<test>
def test():
    assert [/INST]  Sure, here are some test cases for the `sort_array` function:
# test cases for empty array
test_empty_array = [
assert sort_array([]) == []

# test cases for sorted array

test_sorted_array = [3, 2, 1, 4]
assert sort_array(test_sorted_array) == [1, 2, 3, 4]

# test cases for non-sorted array with even num of elements

test_non_sorted_array = [1, 2, 3, 4, 5, 6, 7]
assert sort_array(test_non_sorted_array) == [1, 2, 3, 4, 5, 6, 7]

# test cases for non-sorted array with odd num of elements

test_non_sorted_array = [1, 2, 3, 4, 5, 6, 7, 8]
assert sort_array(test_non_sorted_array) == [1, 2, 3, 4, 5, 