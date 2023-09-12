[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def can_arrange(arr):
    
    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `can_arrange` function:
```
def test_positive():
    # Test with a properly sorted list
    arr = [3, 2, 1, 4]
    assert can_arrange(arr) == 1

def test_negative():
    # Test with a list that is not sorted
    arr = [4, 1, 2, 3]
    assert can_arrange(arr) == -1

def test_edge():
    # Test with a list that is almost sorted
    arr = [3, 2, 1, 4, 4]
    assert can_arrange(arr) == 2

def test_empty():
    # Test with an empty list
    arr = []
    assert can_arrange(arr) == -1

def test_outOfRange():
    # Test with a list that goes out of range
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert can_