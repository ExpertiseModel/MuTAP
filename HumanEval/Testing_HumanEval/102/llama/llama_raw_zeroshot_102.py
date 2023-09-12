[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def choose_num(x, y):
    
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1


# test case
def test():
    assert [/INST]  Sure, I'd be happy to help! Here are some test cases for the `choose_num` function:
```python
def test_choose_num():
    # Test with positive integers
    assert choose_num(3, 4) == 4
    assert choose_num(7, 3) == -1
    # Test with non-integer arguments
    with pytest.raises(TypeError):
        choose_num(3.5, 4.5)
    with pytest.raises(ValueError):
        choose_num(3, "hello")
    # Test edge cases
    assert choose_num(0, 0) == 0
    assert choose_num(1, 1) == 1
    assert choose_num(-1, -1) == -1
    # Test with larger integers
    assert choose_num(10, 5) == 5
    assert choose_num(100, 50) == 50
    # Test with odd and even numbers
    assert choose_num(3, 5) == 3
    assert choose_num(