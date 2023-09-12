[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def add(x: int, y: int):
    
    return x + y




# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `add` function in Python:
```
def test():
    assert add(2, 3) == 5
    assert add(3, 2) == 5
    assert add(5, 0) == 5
    assert add(0, 5) == 0
    assert add(10, 10) == 20
    assert add(-3, -2) == -5
    assert add(-2, -3) == -5
    assert add(10, -2) == 8
    assert add(-10, 10) == -0
    assert add(0, 0) == 0
```
Explanation:
* `assert add(2, 3) == 5`: This test case checks that the function adds 2 and 3 properly and returns 5.
* `assert add(3, 2) == 5`: This test case checks that the function adds 3 and 2 properly and returns 5.
* `assert add(5, 0) == 5`: This test case checks that the