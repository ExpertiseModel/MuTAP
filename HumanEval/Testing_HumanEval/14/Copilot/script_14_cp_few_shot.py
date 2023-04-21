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
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    """
    result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result




#</code>
#<test>

def test_all_prefixes():
    assert all_prefixes('') == ['']
    assert all_prefixes('a') == ['', 'a']
    assert all_prefixes('ab') == ['', 'a', 'ab']
    assert all_prefixes('abc') == ['', 'a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['', 'a', 'ab', 'abc', 'abcd']
    assert all_prefixes('abcde') == ['', 'a', 'ab', 'abc', 'abcd', 'abcde']
    assert all_prefixes('abcdef') == ['', 'a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']
    assert all_prefixes('abcdefg') == ['', 'a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']
    assert all_prefixes('abcdefgh') == ['', 'a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']
    assert all_prefixes('abcdefghi') == ['', 'a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi']
    assert all_prefixes('abcdefghij') == ['', 'a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']
    assert all_prefixes('abcdefghijk') == ['', 'a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk']
    assert all_prefixes('abcdefghijkl') == ['', 'a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl']
    assert all_prefixes('abcdefghijklm') == ['', 'a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm']
    