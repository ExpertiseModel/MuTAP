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
def is_bored(S):
    
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)


#</code>
#<test>
def test():
    assert [/INST]  Sure! Here are some test cases for the `is_bored` function:
# Test positive example
def test_positive():
    S = "I am so bored with this meeting. I can't wait to go home and take a nap."
    assert is_bored(S) == True
# Test negative example
def test_negative():
    S = "I am excited for the weekend. I have a lot of fun plans."
    assert is_bored(S) == False
# Test edge case
def test_edge_case():
    S = "I am so bored with this meeting. I can't wait to go home and take a nap, but I really need to stay awake."
    assert is_bored(S) == True
# Test additional edge cases
def test_additional_edge_cases():
    S = "I am so bored with this meeting, but I really need to stay awake."
    assert is_bored(S) == True
    S = "I am excited for the weekend, but I am also a little bored."
    assert is_bored(