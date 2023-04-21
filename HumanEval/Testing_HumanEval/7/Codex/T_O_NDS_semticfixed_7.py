from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    
    return [x for x in strings if substring in x]




def test():
    assert filter_by_substring(['abcd', 'def', 'ghi'], 'bc') == ['abcd']
    assert filter_by_substring(['abcd', 'def', 'ghi'], 'ef') == ['def']
    assert filter_by_substring(['abcd', 'def', 'ghi'], 'hi') == ['ghi']
    assert filter_by_substring(['abcd', 'def', 'ghi'], 'abcd') == ['abcd']
    assert filter_by_substring(['abcd', 'def', 'ghi'], 'def') == ['def']
    assert filter_by_substring(['abcd', 'def', 'ghi'], 'ghi') == ['ghi']
    assert filter_by_substring(['abcd', 'def','ghi'], 'ghi') == ['ghi']
