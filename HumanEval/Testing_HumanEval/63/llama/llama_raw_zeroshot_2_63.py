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
```
    # Test 1: Valid input
    assert fibfib(0) == 0
    # Test 2: Valid input
    assert fibfib(1) == 0
    # Test 3: Valid input
    assert fibfib(2) == 1
    # Test 4: Input greater than 2
    assert fibfib(3) == 1 + fibfib(2) + fibfib(1)
    # Test 5: Input less than 0
    assert fibfib(-1) == 0
    # Test 6: Input equal to 0
    assert fibfib(0) == 0
    # Test 7: Input greater than maximum value
    assert fibfib(100) == 0
```
Explanation:

* Test 1: Returns the expected value of 0 when passed a valid input of 0.
* Test 2: Returns the expected value of 0 when passed a valid input of 1.
* Test 3: Returns the expected