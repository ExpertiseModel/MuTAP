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
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    
    return [x for x in strings if substring in x]




#</code>
#<test>
def test():
    assert [/INST]  Here are some test cases for the `filter_by_substring` function:

#<testcase>

def test_should_return_elements_that_contain_substring():
    strings = ["Hello", "World", "This is a test", "string contains"]
    result = filter_by_substring(strings, "contains")
    assert result == ["string contains"]
#</testcase>

#<testcase>

def test_should_ignore_case():
    strings = ["Hello", "world", "This Is a TEST", "stringContains"]
    result = filter_by_substring(strings, "test")
    assert result == ["string Contains"]
#</testcase>

#<testcase>

def test_should_return_empty_list_if_substring_is_not_found():
    strings = ["Hello", "World", "This is a test", "not found"]
    result = filter_by_substring(strings, "not found")
    assert result == []
#</testcase>

#<testcase>

def test_should_work