[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]


# test case
def test():
    assert [/INST]  Certainly! Here are some test cases for the `pluck` function:
```
def test_single_element_array():
    arr = [1, 2, 3, 4, 5]
    result = pluck(arr)
    expected = [[1, 2, 3, 4, 5]]
    assert result == expected

def test_empty_array():
    arr = []
    result = pluck(arr)
    expected = [[], None]
    assert result == expected

def test_mixed_array():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = pluck(arr)
    expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    assert result == expected

def test_filter_ Works():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 