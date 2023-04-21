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


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
    """
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1

        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]




#</code>
#<test>

def test_parse_nested_parens():
    assert parse_nested_parens('') == []
    assert parse_nested_parens('()') == [1]
    assert parse_nested_parens('() ()') == [1, 1]
    assert parse_nested_parens('() () ()') == [1, 1, 1]
    assert parse_nested_parens('() () (())') == [1, 1, 2]
    assert parse_nested_parens('() () (()) ()') == [1, 1, 2, 1]
    assert parse_nested_parens('() () (()) () ()') == [1, 1, 2, 1, 1]
    assert parse_nested_parens('() () (()) () () ()') == [1, 1, 2, 1, 1, 1]
    assert parse_nested_parens('() () (()) () () () ()') == [1, 1, 2, 1, 1, 1, 1]
    assert parse_nested_parens('() () (()) () () () () ()') == [1, 1, 2, 1, 1, 1, 1, 1]
    assert parse_nested_parens('() () (()) () () () () () ()') == [1, 1, 2, 1, 1, 1, 1, 1, 1]
    assert parse_nested_parens('() () (()) () () () () () () ()') == [1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
    assert parse_nested_parens('() () (()) () () () () () () () ()') == [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    assert parse_nested_parens('() () (()) () () () () () () () () ()') == [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert parse_nested_parens('() () (()) () () () () () () () () () ()') == [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    


