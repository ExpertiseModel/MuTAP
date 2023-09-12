[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def closest_integer(value):
    
    from math import floor, ceil

    if value.count('.') == 1:
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res



# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `closest_integer` function:
```
# Test 1: Positive integer input
value = 5.5
assert closest_integer(value) == 6

# Test 2: Negative integer input
value = -5.5
assert closest_integer(value) == -6

# Test 3: Non-decimal input
value = 'apple'
assert closest_integer(value) == 0

# Test 4: Trailing zeros
value = 5.50
assert closest_integer(value) == 6

# Test 5: Half-integer input
value = 5.5
assert closest_integer(value) == 6

# Test 6: Non-integer input
value = '5.5abc'
assert closest_integer(value) == 0
```
Explanation:

* Test 1: Positive integer input: The function should return the closest integer to 5.5.
* Test 2: Negative integer input: The function should return the closest integer to -5.5.
* Test 3