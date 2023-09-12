[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def monotonic(l: list):
    
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False




# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `monotonic` function in Python:

```
# test non-empty list
test_list = [1, 2, 3, 4, 5]
assert monotonic(test_list) == True

# test empty list
test_list = []
assert monotonic(test_list) == False

# test sorted list
test_list = [1, 2, 3, 4, 5].sort()
assert monotonic(test_list) == True

# test mixed-order list
test_list = [1, 3, 4, 2, 5]
assert monotonic(test_list) == False

# test reversed list
test_list = [1, 3, 4, 2, 5].reverse()
assert monotonic(test_list) == True

# test nested lists
test_list = [1, 2, [3, 4], 5]
assert monotonic(test_list) == True

# test duplicates
test_list = [1, 2, 