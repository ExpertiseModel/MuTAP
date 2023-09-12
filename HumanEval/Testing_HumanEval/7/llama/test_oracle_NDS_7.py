from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    
    return [x for x in strings if substring in x]




# test case
def test():
    # Test that the function returns a list of strings that contain the substring 'abc'
    assert filter_by_substring(['hello', 'world', 'abc'], 'abc') == ['abc']

    # Test that the function ignores case
    assert filter_by_substring(['hello', 'World', 'abc'], 'Abc') == ['abc']

    # Test that the function works with multiple substrings
    assert filter_by_substring(['hello', 'world', 'abc', 'def'], 'abc', 'def') == ['abc', 'def']


    # Test that the function raises a ValueError if the input list is empty
    assert