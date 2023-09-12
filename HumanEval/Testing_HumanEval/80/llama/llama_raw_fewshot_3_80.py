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
def is_happy(s):
    
    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
        return False
    return True


#</code>
#<test>
def test():
    assert [/INST]  Great! Here are some test cases for the `is_happy` function:
# Test case 1: Happy strings
s = "HelloWorld"
assert is_happy(s) == True

# Test case 2: Happy strings with repeated characters
s = "HelloHello"
assert is_happy(s) == True

# Test case 3: Happy strings with adjacent repeating characters
s = "HelloWorldHello"
assert is_happy(s) == True

# Test case 4: Unhappy strings with gaps
s = "Hello World"
assert is_happy(s) == False

# Test case 5: Unhappy strings with adjacent repeating characters
s = "HelloWorldHello"
assert is_happy(s) == False

# Test case 6: Unhappy strings with duplicates in the middle
s = "HelloHelloWorld"
assert is_happy(s) == False

# Test case 7: Happy strings with different lenghts
s1 = "Hello"
s2 = "World"
assert is_happy(s1) == True
assert