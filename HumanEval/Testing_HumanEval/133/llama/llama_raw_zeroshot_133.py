[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def sum_squares(lst):
    
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared


# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `sum_squares` function:
```
# Test 1: Simple list with positive integers
lst = [1, 2, 3, 4, 5]
assert sum_squares(lst) == 15

# Test 2: List with negative integers
lst = [-1, -2, -3, -4, -5]
assert sum_squares(lst) == -15

# Test 3: List with floating-point numbers
lst = [3.14, 2.7, 1.8, 0.5, -0.2]
assert sum_squares(lst) == 12.5859375

# Test 4: List with empty list
lst = []
assert sum_squares(lst) == 0

# Test 5: List with invalid element
lst = [1, 2, 3, 4, "apple"]
assert sum_squares(lst) == None

# Test 6: List with large numbers
lst = [10000,