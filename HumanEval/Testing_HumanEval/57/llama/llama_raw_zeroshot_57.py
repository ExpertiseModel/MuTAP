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
    assert [/INST]  Great! Here are some test cases for the `monotonic` function:
```py
def test_monotonic_empty_list():
    assert monotonic([]) == True

def test_monotonic_sorted_list():
    assert monotonic([1, 2, 3]) == True

def test_monotonic_sorted_reverse_list():
    assert monotonic([3, 2, 1]) == True

def test_monotonic_partially_sorted_list():
    assert monotonic([1, 3, 2]) == False

def test_monotonic_partially_sorted_reverse_list():
    assert monotonic([2, 1, 3]) == False

def test_monotonic_mixed_list():
    assert monotonic([1, 2, 3, 4, 5]) == False

def test_monotonic_mixed_reverse_list():
    assert monotonic([5, 4, 3, 2, 1]) == False
```
Explanation:

* `test_monot