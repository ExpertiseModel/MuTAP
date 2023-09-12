[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))


# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `sort_array` function:
```python
def test():
    # Test with non-negative integers
    arr = [1, 5, 2, 3, 4]
    assert sort_array(arr) == [1, 2, 3, 4, 5]
    arr = [-2, -3, -4, -5, -6]
    assert sort_array(arr) == [-6, -5, -4, -3, -2]
    arr = [1, 0, 2, 3, 4]
    assert sort_array(arr) == [0, 1, 2, 3, 4]
    # Test with negative integers
    arr = [-1, -5, -2, -3, -4]
    assert sort_array(arr) == [-4, -3, -2, -1, -5]
    # Test with floating point numbers
    arr = [1.5, 2.3, 3.1, 4.2, 5.5]
   