from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    
    return [x for x in strings if x.startswith(prefix)]




# test case

def test():
    assert filter_by_prefix([], "") == []
    assert filter_by_prefix(["apple", "banana", "cherry"], "a") == ["apple"]
