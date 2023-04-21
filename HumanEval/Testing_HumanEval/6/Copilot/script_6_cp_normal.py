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





 # generate test case for the function above

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
   