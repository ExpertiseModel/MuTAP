[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def is_simple_power(x, n):
    
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x) 


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `is_simple_power` function:
```
def test1():
    x = 2
    n = 3
    assert is_simple_power(x, n) == False
    x = 4
    n = 2
    assert is_simple_power(x, n) == False
    x = 8
    n = 3
    assert is_simple_power(x, n) == True

def test2():
    x = 1
    n = 2
    assert is_simple_power(x, n) == True
    x = 10
    n = 3
    assert is_simple_power(x, n) == False

def test3():
    x = -1
    n = 2
    assert is_simple_power(x, n) == False
    x = 0
    n = 3
    assert is_simple_power(x, n) == True

def test4():
    x = 100
    n = 2
    assert is_simple_power