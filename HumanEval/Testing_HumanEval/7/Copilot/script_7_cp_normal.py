from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    """
    return [x for x in strings if substring in x]






 # generate test case for the function above

def test_filter_by_substring():
    assert filter_by_substring(["abc", "bcd", "cde"], "ab") == ["abc"]
    assert filter_by_substring(["abc", "bcd", "cde"], "de") == ["cde"]
    assert filter_by_substring(["abc", "bcd", "cde"], "xx") == []
    assert filter_by_substring(["a", "b", "c"], "a") == ["a"]
    assert filter_by_substring(["a", "b", "c"], "b") == ["b"]
    assert filter_by_substring(["a", "b", "c"], "c") == ["c"]
    assert filter_by_substring(["a", "b", "c"], "d") == []
    assert filter_by_substring(["a", "b", "c"], "ab") == []
    assert filter_by_substring(["a", "b", "c"], "abc") == []
    assert filter_by_substring(["a", "b", "c"], "d") == []