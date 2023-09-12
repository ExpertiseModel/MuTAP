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
    assert [/INST]  Sure, here are some test cases for the `pluck` function:
```python
def test_pluck_empty_array():
    arr = []
    result = pluck(arr)
    assert result == []

def test_pluck_non_even_numbers():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = pluck(arr)
    assert result == []

def test_pluck_single_even_number():
    arr = [2, 4, 6, 8, 10]
    result = pluck(arr)
    assert result == [2]

def test_pluck_multi_even_numbers():
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18]
    result = pluck(arr)
    assert result == [4, 6, 8, 10]

def test_pluck_arr_index_non_exist():
   