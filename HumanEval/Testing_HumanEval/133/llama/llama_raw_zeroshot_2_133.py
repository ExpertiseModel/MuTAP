[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared


# test case
def test():
    assert [/INST]  Great! Here are some test cases for the `sum_squares` function:
```python
# Test 1: Positive integers
lst = [1, 2, 3]
assert sum_squares(lst) == 14

# Test 2: Non-integral numbers
lst = [1.4, 4.2, 0]
assert sum_squares(lst) == 29

# Test 3: Negative integers
lst = [-2.4, 1, 1]
assert sum_squares(lst) == 6

# Test 4: List with floating point numbers
lst = [1.2, 3.4, 0.9]
assert sum_squares(lst) == 30.8

# Test 5: List with empty elements
lst = [1, 2, None, 4]
assert sum_squares(lst) == 10

# Test 6: List with duplicate elements
lst = [1, 2, 2, 3]
assert sum_squares(lst) == 14

