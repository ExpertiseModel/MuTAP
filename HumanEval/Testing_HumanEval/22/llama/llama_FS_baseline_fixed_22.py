from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    
    return [x for x in values if isinstance(x, int)]




#</code>
#<test>

def test():
    assert filter_integers([1, 2, 3, 4, 5, 'hello']) == [1, 2, 3, 4, 5]
    assert filter_integers([1, 2, 3, 4, 5, 'hello']) == [1, 2, 3, 4, 5]
