from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s





 # generate test case for the function above

def test_longest():
    assert longest(["a", "ab", "abc"]) == "abc"
    assert longest(["a", "ab", "abc", "abcd"]) == "abcd"
    assert longest(["a", "ab", "abc", "abcd", "abcde"]) == "abcde"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef"]) == "abcdef"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg"]) == "abcdefg"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh"]) == "abcdefgh"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi"]) == "abcdefghi"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij"]) == "abcdefghij"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk"]) == "abcdefghijk"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk", "abcdefghijkl"]) == "abcdefghijkl"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk", "abcdefghijkl", "abcdefghijklm"]) == "abcdefghijklm"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk", "abcdefghijkl", "abcdefghijklm", "abcdefghijklmn"]) == "abcdefghijklmn"
    assert longest(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk", "abcdefghijkl", "abcdefghijklm", "abcdefghijklmn", "abcdefghijklmno"]) == "abcdefghijklmno"
