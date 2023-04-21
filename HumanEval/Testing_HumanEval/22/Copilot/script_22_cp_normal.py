from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}



 # generate test case for the function above

def test_filter_integers():
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert filter_integers([1.0, 2.0, 3.0, 4.0, 5.0]) == []
    assert filter_integers([1.0, 2, 3.0, 4, 5.0]) == [2, 4]
    assert filter_integers(["1", "2", "3", "4", "5"]) == []
    assert filter_integers(["1", "2", "3", "4", "5", 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert filter_integers([True, False, 1, 0]) == [1, 0]
    assert filter_integers([True, False, 1, 0, "1", "0"]) == [1, 0]
    assert filter_integers([True, False, 1, 0, "1", "0", "True", "False"]) == [1, 0]
    assert filter_integers([True, False, 1, 0, "1", "0", "True", "False", 0.0, 0.1]) == [1, 0]
    assert filter_integers([True, False, 1, 0, "1", "0", "True", "False", 0.0, 0.1, 1.0, 2.0, 3.0]) == [1, 0]
    assert filter_integers([True, False, 1, 0, "1", "0", "True", "False", 0.0, 0.1, 1.0, 2.0, 3.0, 1.1, 1.2, 1.3]) == [1, 0]