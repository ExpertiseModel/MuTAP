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
    assert [/INST]  Sure, here are some test cases for the `is_simple_power` function:
```python
def test_valid_inputs():
    # Test with valid inputs
    assert is_simple_power(2, 3) == False
    assert is_simple_power(3, 3) == True
    assert is_simple_power(5, 5) == True
    assert is_simple_power(-1, 3) == False
    assert is_simple_power(0, 3) == False

def test_edge_cases():
    # Test with edge cases
    assert is_simple_power(1, 1) == True
    assert is_simple_power(1, 2) == False
    assert is_simple_power(0, 1) == False
    assert is_simple_power(-1, 1) == False

def test_large_nums():
    # Test with large numbers
    assert is_simple_power(10, 3) == False
    assert is_simple_power(100, 3) == False
    assert is_simple