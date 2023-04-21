from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    
    return [x for x in values if isinstance(x, int)]



def test():
    assert filter_integers([1,2,3,4, 'a', 'b', 'c', 4, 5]) == [1,2,3,4, 4]
