from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    """
    return [x for x in strings if x.startswith(prefix)]


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}



 # generate test case for the function above

def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == []
    assert filter_by_prefix(['a', 'b'], 'a') == ['a']
    assert filter_by_prefix(['a', 'b'], 'b') == ['b']
    assert filter_by_prefix(['a', 'b', 'c'], 'a') == ['a']
    assert filter_by_prefix(['a', 'b', 'c'], 'b') == ['b']
    assert filter_by_prefix(['a', 'b', 'c'], 'c') == ['c']
    assert filter_by_prefix(['a', 'b', 'c'], 'd') == []
    assert filter_by_prefix(['a', 'b', 'c'], '') == ['a', 'b', 'c']
    assert filter_by_prefix(['a', 'b', 'c'], 'ab') == []