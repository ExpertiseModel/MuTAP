[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def greatest_common_divisor(a: int, b: int) -> int:
    
    while b:
        a, b = b, a % b
    return a




# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `greatest_common_divisor` function using Python:
```python
def test_gcd_empty_args():
    assert greatest_common_divisor() == 1

def test_gcd_zero_arg():
    assert greatest_common_divisor(0) == 1

def test_gcd_negative_args():
    assert greatest_common_divisor(-1, 2) == 1
    assert greatest_common_divisor(-2, 1) == 2

def test_gcd_large_args():
    assert greatest_common_divisor(10, 20) == 5
    assert greatest_common_divisor(30, 40) == 10

def test_gcd_random_args():
    assert greatest_common_divisor(10, 30) == 10
    assert greatest_common_divisor(4, 16) == 4

def test_gcd_edge_cases():
    assert