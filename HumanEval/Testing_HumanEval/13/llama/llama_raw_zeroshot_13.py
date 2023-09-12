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
    assert [/INST]  Sure! Here are some test cases for the `greatest_common_divisor` function:
```
def test_gcd_integer_divisors():
    assert greatest_common_divisor(6, 8) == 2
    assert greatest_common_divisor(10, 20) == 5

def test_gcd_unequal_ integers():
    assert greatest_common_divisor(6, -8) == 2
    assert greatest_common_divisor(10, -20) == 5

def test_gcd_negative_numbers():
    assert greatest_common_divisor(-6, 8) == -2
    assert greatest_common_divisor(-10, -20) == -5

def test_gcd_zero():
    assert greatest_common_divisor(0, 8) == 0
    assert greatest_common_divisor(0, -20) == 0

def test_gcd_empty():
    assert greatest_common_divisor( [], 8