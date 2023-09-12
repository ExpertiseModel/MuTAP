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
    assert [/INST]  Sure! Here are some test cases for the `starts_one_ends` function:
```
# Test 1: Valid input
n = 2
assert starts_one_ends(n) == 18 * (10 ** (n - 2)) == 54

# Test 2: Zero input
n = 0
assert starts_one_ends(n) == 1

# Test 3: Negative input
n = -1
assert starts_one_ends(n) == 0

# Test 4: Large input
n = 100
assert starts_one_ends(n) == 190416000

# Test 5: edge case tests
n = 1
assert starts_one_ends(n) == 18 * (10 ** (n - 2)) == 1
n = 2
assert starts_one_ends(n) == 18 * (10 ** (n - 2)) == 54
n = 3
assert starts_one_ends(n) == 18 * (10