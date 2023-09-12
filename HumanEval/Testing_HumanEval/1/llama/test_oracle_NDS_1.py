from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    result = []
    current_string = []
    current_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)

            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    return result

def test():
    # Test empty string
    assert separate_paren_groups("") == []
    # Test simple paren group
    assert separate_paren_groups("(foo)") == ["(foo)"]
    # Test nested paren groups
    assert separate_paren_groups ("((foo))") == ["((foo))"]
    # Test comments
    assert separate_paren_groups ("foofoo(bar)") == ["(bar)"]
    # Test empty string after paren group
    assert separate_paren_groups ("foo(bar)") == ["(bar)"]
    # Test multiple paren groups
    assert separate_paren_groups ("(foo)(bar)") == ["(foo)", "(bar)"]
    # Test invalid input
    assert separate_paren_groups ("foo((bar)qux)") == ["((bar)qux)"]
