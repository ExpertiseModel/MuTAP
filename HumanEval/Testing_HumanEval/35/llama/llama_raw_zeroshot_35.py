[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def max_element(l: list):
    
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `max_element` function:
```
# Test 1: Valid list
l = [1, 2, 3, 4, 5]
assert max_element(l) == 5

# Test 2: Multiple maximum elements
l = [1, 2, 3, 4, 5, 5]
assert max_element(l) == 5

# Test 3: Negative values
l = [1, -2, -3, -4, -5]
assert max_element(l) == -5

# Test 4: List with no elements
l = []
assert max_element(l) == None

# Test 5: List with duplicates
l = [1, 2, 2, 3, 3, 3]
assert max_element(l) == 3

# Test 6: List with leading duplicates
l = [1, 2, 2, 3, 3, 3]
assert max_element(l) == 3

# Test 7: List with