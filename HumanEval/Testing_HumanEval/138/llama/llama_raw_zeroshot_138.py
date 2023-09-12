[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def is_equal_to_sum_even(n):
    
    return n%2 == 0 and n >= 8


# test case
def test():
    assert [/INST]  Certainly! Here are some test cases for the `is_equal_to_sum_even` function in Python:

```
# Test 1: Negative numbers
n = -10
assert not is_equal_to_sum_even(n)

# Test 2: Non-negative numbers less than or equal to 8
n = 7
assert is_equal_to_sum_even(n)

# Test 3: Non-negative numbers greater than 8
n = 12
assert not is_equal_to_sum_even(n)

# Test 4: Zero
n = 0
assert is_equal_to_sum_even(n)

# Test 5: Irrational numbers
n = π
assert not is_equal_to_sum_even(n)

# Test 6: Floating point numbers
n = 3.14
assert not is_equal_to_sum_even(n)

# Test 7: Fraction numbers
n = 1/2
assert not is_equal_to_sum_even(n