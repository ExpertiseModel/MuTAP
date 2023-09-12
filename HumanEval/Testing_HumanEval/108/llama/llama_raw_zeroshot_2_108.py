[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))


# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `count_nums` function in Python:
testing.py:
```
def test_empty_array():
    result = count_nums([])
    assert result == 0

def test_array_with_negative_numbers():
    result = count_nums([-1, 11, -11])
    assert result == 1

def test_array_with_positive_numbers():
    result = count_nums([1, 1, 2])
    assert result == 3

def test_array_with_mix_of_positive_and_negative():
    result = count_nums([-2, 3, -1, 1, 2])
    assert result == 3

def test_empty_array_with_leading_spaces():
    result = count_nums(["   ", "-1", " 11", "-11"])
    assert result == 1

def test_with_integer_numbers():
    result = count_nums([1, 2, 3])
