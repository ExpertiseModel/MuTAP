
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s




# test case
def test():
    # Test 1: Ensure the function returns the longest string in the list
    assert longest(["hello", "world", "python"]) == "python"

    # Test 2: Ensure the function returns None when the list is empty
    assert longest([]) is None

    # Test 3: Ensure the function works correctly for lists of different strings
    assert longest(["hello", 1, "world", ]) == "world"

    # Test 4: Ensure the function works correctly for lists of duplicate strings
    assert longest(["hello", "hello", "world"]) == "hello"

    # Test 5: Ensure the function works correctly for lists of very long strings
    assert longest(["hello", "world", "the", "longest", "string", "in", "the", "list"]) == "the longest string in the list"

    # Test 6: Ensure the function works correctly for lists of strings with different lengths
   
    assert longest(["hello", "world", "python"]) == "python"