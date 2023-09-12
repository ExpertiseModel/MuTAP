[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    
    return [x for x in values if isinstance(x, int)]




# test case
def test():
    assert [/INST]  Sure, I'd be happy to help! Here are some test cases for the `filter_integers` function:
```
def test_empty_list():
    values = []
    result = filter_integers(values)
    assert result == []

def test_integer_list():
    values = [1, 2, 3, 4, 5]
    result = filter_integers(values)
    assert result == [1, 2, 3, 4, 5]

def test_non_integer_list():
    values = [1.0, "hello", 3.5, 4.0, 5.0]
    result = filter_integers(values)
    assert result == [1, 3, 4, 5]

def test_list_of_lists():
    values = [[1, 2], ["hello", "world"], [3.0, 4.0], [5.0, 6.0]]
    result = filter_integers(values)
    assert result == [[1, 3], ["hello", "