[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def fib(n: int):
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `fib` function:
```
def test_fib_single_call():
    assert fib(1) == 1
def test_fib_small_values():
    for n in range(1, 5):
        assert fib(n) == fib.fib(n)
def test_fib_large_values():
    for n in range(10, 20):
        assert fib(n) == round(fib.fib(n), 4)
def test_fib_neg_input():
    with pytest.raises(TypeError):
        fib(-1)
def test_fib_failure():
    with pytest.raises(ValueError):
        fib(100)
```
Explanation:

* `test_fib_single_call()` tests that `fib(1)` returns `1`.
* `test_fib_small_values()` tests that `fib(n)` returns the correct value for small values of `n`.
* `test_fib_large_values