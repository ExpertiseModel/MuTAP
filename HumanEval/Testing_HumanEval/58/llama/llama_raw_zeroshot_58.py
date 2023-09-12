[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def common(l1: list, l2: list):
    
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `common` function in Python:
```python
def test():
    # Test with empty lists
    assert common([], []) == []
    assert common([], [1, 2, 3]) == [1, 2, 3]
    # Test with different lengths
    assert common([1, 2, 3], [2, 3, 4]) == [1, 2]
    assert common([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    # Test with duplicates
    assert common([1, 2, 2], [2, 3, 4]) == [1, 2, 3]
    # Test with complex data structures
    assert common([(1, 'a')], [((1, 'a'), (2, 'b')], (3, 'c')]) == [((1, 'a'), (3, 'c'])])
    # Test with different types
    assert common([1], ['a']) == ['