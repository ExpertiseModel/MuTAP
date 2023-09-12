[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 These are two examples of codes and their tests.

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
#</test>

#<original code>



from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

print(string_xor('1011101', '1011101'))



#</original code>

generate test in the form of above example tests for the original code:

#<test>
def test():
    assert [/INST]  Sure, I'd be happy to help! Here are some tests for the `string_xor` function:
#<test>

from typing import List
def test_string_xor() -> None:
    # Test basic functionality
    assert string_xor('010', '110') == '100'
    assert string_xor('0', '1') == '0'
    assert string_xor('1', '0') == '1'
    # Test edge cases
    assert string_xor('0', '0') == '0'
    assert string_xor('10', '10') == '10'
    assert string_xor('0', '11') == '1'
    # Test different input lengths
    assert string_xor('0', '000100') == '0000100'
    assert string_xor('1', '000100') == '000100'
    assert string_xor('0', '111000') == '11