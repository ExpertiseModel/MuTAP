[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `sort_array` function in Python:
```python
def test_sort_array():
    # Test with empty array
    assert sort_array([]) == []
    # Test with valid array
    arr = [1, 2, 3, 4, 5]
    assert sort_array(arr) == [1, 2, 3, 4, 5]
    # Test with different number of elements
    arr = [1, 2, 3, 4, 5, 6]
    assert sort_array(arr, reverse=(arr[0] + arr[-1]) % 2 == 0) == [1, 2, 3, 4, 5, 6]
    # Test with arrays of different types
    arr = [1, 2, 3, 4, 5]
    assert sort_array(arr, reverse=(arr[0] + arr[-1]) % 2 == 0) == [1, 2, 3, 4, 5]
    # Test with arrays of different sizes
