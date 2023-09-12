[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)


# test case
def test():
    assert [/INST]  Here are some test cases for the `order_by_points` function:
```python
# Test basic functionality
assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
# Test empty list
assert order_by_points([]) == []
# Test with negative numbers
assert order_by_points([-1, -11, 1, -12, 11]) == [-1, -11, 1, -12, 11]
# Test with very large numbers
assert order_by_points([10000, 1000000, -10000, -1000000, -10000000]) == [-10000, -100000, 10000, 1000000, 10000000]
# Test with very small numbers
assert order_by_points([0.1, 0.