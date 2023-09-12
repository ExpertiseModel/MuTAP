[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def sort_array(arr):
    
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))


# test case
def test():
    assert [/INST]  Great, I'd be happy to help you generate test cases for the `sort_array` function! Here are some test cases you can use:
```python
def test_sort_array_empty_array():
    arr = []
    result = sort_array(arr)
    assert result == []

def test_sort_array_random_array():
    arr = [2, 6, 3, 1, 4]
    result = sort_array(arr)
    assert result == [1, 2, 3, 4, 6]

def test_sort_array_array_with_ duplicates():
    arr = [2, 2, 6, 3, 1, 4]
    result = sort_array(arr)
    assert result == [1, 2, 2, 3, 4, 6]

def test_sort_array_array_with_ strings():
    arr = ['a', 'b', 'c', 'd', 'e', 'f']
    result = sort_array(arr)
    assert result == ['a', '