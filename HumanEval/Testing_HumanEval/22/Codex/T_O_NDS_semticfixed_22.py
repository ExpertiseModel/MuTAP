from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    
    return [x for x in values if isinstance(x, int)]




def test():
    assert filter_integers([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert filter_integers([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert filter_integers([1, 2, 3, 4, 'Hello']) == [1, 2, 3, 4]
    assert filter_integers([1.1, 2.2, 3.3, 4.4, 5.5, 6.6]) == []
    assert filter_integers([1, 'Hello', 3, 4, 5, 6]) == [1, 3, 4, 5, 6]
