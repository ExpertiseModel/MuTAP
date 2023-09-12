[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def maximum(arr, k):
    
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `maximum` function:
```
def test_empty_array():
    arr = []
    k = 3
   actual = maximum(arr, k)
   expected = []
    assert actual == expected

def test_small_array():
    arr = [1, 2, 3]
    k = 2
    actual = maximum(arr, k)
    expected = [2, 3]
    assert actual == expected

def test_large_array():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 4
    actual = maximum(arr, k)
    expected = [4, 5, 6, 7]
    assert actual == expected

def test_negative_k():
    arr = [1, 2, 3]
    k = -3
    actual = maximum(arr, k)
    expected = []
    assert actual == expected

def test_ invalid_type():
    arr =