from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]





def test():
    assert filter_by_substring(['hello', 'world', 'python', 'is', 'awesome'], 'python') == ['python']
    assert filter_by_substring(['hello', 'world', 'python', 'is', 'awesome'], 'awesome') == ['awesome']
    assert filter_by_substring(['hello', 'world', 'python', 'is', 'awesome'], 'world') == ['world']
    assert filter_by_substring(['hello', 'world', 'python', 'is', 'awesome'], 'hello') == ['hello']
    assert filter_by_substring(['hello', 'world', 'python', 'is', 'awesome'], 'is') == ['is']
