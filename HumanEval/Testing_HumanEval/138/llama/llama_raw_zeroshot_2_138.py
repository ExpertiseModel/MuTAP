[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n%2 == 0 and n >= 8


# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `is_equal_to_sum_even` function:
```python
# Test positive numbers
assert is_equal_to_sum_even(2) == False
assert is_equal_to_sum_even(4) == False
assert is_equal_to_sum_even(6) == False

# Test negative numbers
assert is_equal_to_sum_even(-2) == False
assert is_equal_to_sum_even(-4) == False
assert is_equal_to_sum_even(-6) == False

# Test larger numbers
assert is_equal_to_sum_even(8) == True
assert is_equal_to_sum_even(10) == False
assert is_equal_to_sum_even(12) == False

# Test even numbers that cannot be written as sum of 4 even numbers
assert is_equal_to_sum_even(24) == False
assert is_equal_to_sum_even(26) == False

# Test odd numbers
assert is_equal_to_sum_