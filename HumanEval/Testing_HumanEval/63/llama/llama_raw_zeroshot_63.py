[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def fibfib(n: int):
    
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `fibfib` function:
```python
def test_fibfib_single_call():
    assert fibfib(3) == 2

def test_fibfib_negative_input():
    with pytest.raises(ValueError):
        fibfib(-1)

def test_fibfib_zero_input():
    with pytest.raises(ZeroDivisionError):
        fibfib(0)

def test_fibfib_edge_cases():
    assert fibfib(1) == 1
    assert fibfib(2) == 2
    assert fibfib(3) == 3
    with pytest.raises(ZeroDivisionError):
        fibfib(4)
```
Explanations:

* `test_fibfib_single_call`: Tests that `fibfib(3)` returns the correct value of 2.
* `test_fibfib_negative_input`: Tests that an invalid input (i.e. a negative