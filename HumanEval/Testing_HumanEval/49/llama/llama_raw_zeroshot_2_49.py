[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def modp(n: int, p: int):
    
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret




# test case
def test():
    assert [/INST]  Great, here are some test cases for the `modp` function:
```
# Test 1: Positive integer inputs
n = 5
p = 7
result = modp(n, p)
assert result == 2

# Test 2: Negative integer input
n = -3
p = 7
result = modp(n, p)
assert result == -2

# Test 3: Zero input
n = 0
p = 7
result = modp(n, p)
assert result == 0

# Test 4: Divisibility
n = 12
p = 3
result = modp(n, p)
assert result == 0

# Test 5: Irrational input
n = 15.5
p = 7.5
result = modp(n, p)
assert result == 4

# Test 6: Large numbers
n = 1000
p = 100
result = modp(n, p)
assert result == 0

# Test 7: Edge cases
