[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def max_fill(grid, capacity):
    import math
    
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `max_fill` function:
```
# Test 1: Valid grid, valid capacity
grid = [1, 2, 3, 4, 5]
capacity = 2
assert max_fill(grid, capacity) == 7

# Test 2: Valid grid, invalid capacity
grid = [1, 2, 3, 4, 5]
capacity = 3
assert max_fill(grid, capacity) == 5

# Test 3: Invalid grid
grid = [1, 2, 3, 4, 5, 6, 7, 8]
capacity = 2
assert max_fill(grid, capacity) == 6

# Test 4: Valid grid, valid capacity
grid = [1, 2, 3, 4, 5]
capacity = 3
assert max_fill(grid, capacity) == 6

# Test 5: Valid grid, invalid capacity
grid = [1, 2, 3, 4, 5]
capacity = 4