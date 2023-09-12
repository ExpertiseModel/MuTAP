from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    
    return [x for x in strings if x.startswith(prefix)]




# test case
def test():
    #test_filter_by_prefix_empty_list
    assert filter_by_prefix([], "") == []

    #test_filter_by_prefix_empty_prefix
    assert filter_by_prefix(["apple", "banana", "cherry"], "") == ["apple", "cherry"]

    #test_filter_by_prefix_single_match
    assert filter_by_prefix(["apple", "banana", "cherry"], "a") == ["apple"]
