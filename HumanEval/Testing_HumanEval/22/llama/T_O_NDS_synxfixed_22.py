
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    
    return [x for x in values if isinstance(x, int)]




# test case
def test():
    #test_empty_list
    assert filter_integers([]) == []

    #test_integer_list
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    #test_non_integer_list
    assert filter_integers([1.0, "hello", 3.5, 4.0, 5.0]) == [1, 3, 4, 5]

    #test_list_of_lists():