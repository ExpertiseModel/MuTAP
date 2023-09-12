[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def add(x: int, y: int):
    
    return x + y




# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `add` function:

```
def test():
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    with pytest.raises(TypeError):
        add(1, "hello")
    with pytest.raises(TypeError):
        add(0, float(0))
```
Let me explain each test case:

* `assert add(1, 2) == 3`: This test case checks that the `add` function returns the correct result when given two integers `1` and `2`.
* `assert add(2, 3) == 5`: This test case checks that the `add` function returns the correct result when given two integers `2` and `3`.
* `assert add(-1, 1) == 0`: This test case checks that the `add` function returns the correct result when given a negative number `-1` and a positive number `1`.
* `