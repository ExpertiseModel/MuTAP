[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def largest_divisor(n: int) -> int:
    
    for i in reversed(range(n)):
        if n % i == 0:
            return i




# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `largest_divisor` function:

```
def test_edge_cases():
    assert largest_divisor(1) == 1
    assert largest_divisor(2) == 2
    assert largest_divisor(3) == 3

def test_small_numbers():
    for n in range(1, 10):
        assert largest_divisor(n) == n

def test_large_numbers():
    for n in range(100, 1000):
        assert largest_divisor(n) == n

def test_negative_numbers():
    for n in range(-10, 0):
        assert largest_divisor(n) == n

def test_zero():
    assert largest_divisor(0) == 1

def test_inf():
    assert largest_divisor(float('inf')) == float('inf')
```
Note: These test cases cover various edge cases, small and large numbers, negative numbers, and zero. You can add