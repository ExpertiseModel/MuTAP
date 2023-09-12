[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def string_sequence(n: int) -> str:
    
    return ' '.join([str(x) for x in range(n + 1)])




# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `string_sequence` function:
```python
def test():
    # Test with small input
    assert string_sequence(3) == '123'
    # Test with large input
    assert string_sequence(10) == '1234567789'
    # Test with negative input
    with pytest.raises(ValueError):
        string_sequence(-1)
    # Test with non-numeric input
    with pytest.raises(TypeError):
        string_sequence('abc')
```
Explanation:

* In the first test, we pass `n=3` to the `string_sequence` function and assert that the returned string is `123`.
* In the second test, we pass `n=10` to the `string_sequence` function and assert that the returned string is `1234567789`.
* In the third test, we pass `-1` to the `string_sequence` function and assert that a `ValueError` is raised.
* In the fourth test, we