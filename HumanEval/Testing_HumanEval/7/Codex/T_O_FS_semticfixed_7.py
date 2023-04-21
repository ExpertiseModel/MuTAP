from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    
    return [x for x in strings if substring in x]




def test():
    assert filter_by_substring(["John", "Adams", "Jesse"], "s") == ['Adams', 'Jesse']
    assert filter_by_substring(["John", "Adams", "Jesse"], "jo") == []
    assert filter_by_substring(["John", "Adams", "Jesse"], "j") == []
    assert filter_by_substring(["John", "Adams", "Jesse"], "J") == ['John', 'Jesse']
