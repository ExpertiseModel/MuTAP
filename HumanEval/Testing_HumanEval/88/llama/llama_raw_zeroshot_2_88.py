[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `sort_array` function:
```
def test_empty_array():
    assert sort_array([]) == []

def test_unique_array():
    arr = [1, 2, 3, 3, 4, 5]
    assert sort_array(arr) == [1, 2, 3, 4, 5]

def test_negative_value():
    arr = [-1, 2, 3, 4, 5]
    assert sort_array(arr) == [-1, 2, 3, 4, 5]

def test_zero_value():
    arr = [0, 1, 2, 3, 4, 5]
    assert sort_array(arr) == [0, 1, 2, 3, 4, 5]

def test_even_odd():
    arr = [1, 2, 3, 3, 4, 5, 5, 6, 7]
    assert sort_array(arr) == [