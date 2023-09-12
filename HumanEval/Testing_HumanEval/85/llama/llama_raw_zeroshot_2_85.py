[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `add` function:
```
# Test no arguments passed
assert add(()) == []

# Test single list passed
assert add([1, 2, 3, 4, 5]) == [1, 3, 5]

# Test two lists passed
def list1([1, 2, 3, 4, 5]):
    assert add(list1()) == [1, 3, 5]

# Test two lists of different lengths passed
def list2([6, 7, 8, 9, 10]):
    assert add(list2()) == [6, 8, 10]

# Test negative index passed
assert add([1, 2, 3]) == [1, 2, 3]

# Test invalid percentage passed
def invalid_lst([1, 2, 3, 4, 5], 0.5):
    assert add(invalid_lst) == []

# Test empty list passed
assert add([]) == []
```
Please note that these test cases cover