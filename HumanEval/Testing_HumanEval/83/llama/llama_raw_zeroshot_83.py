[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def starts_one_ends(n):
    
    if n == 1: 
        return 1
    return 18 * (10 ** (n - 2))


# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `starts_one_ends` function:
```
# Test 1: Check the function works for small inputs
n = 1
assert starts_one_ends(n) == 1

# Test 2: Check the function works for medium inputs
n = 5
assert starts_one_ends(n) == 70

# Test 3: Check the function works for large inputs
n = 10
assert starts_one_ends(n) == 1400

# Test 4: Check the function returns the correct value for 1
n = 1
assert starts_one_ends(n) == 1

# Test 5: Check the function returns the correct value for very large inputs
n = 20
assert starts_one_ends(n) == 3628800

# Test 6: Check the function raises a ValueError for invalid inputs
n = -1
assert not starts_one_ends(n)

# Test 7: Check the function raises a ValueError for very large inputs
n = 