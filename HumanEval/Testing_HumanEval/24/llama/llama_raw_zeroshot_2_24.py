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
def test_positive_integer():
    n = 10
    result = largest_divisor(n)
    assert result == 5

def test_negative_integer():
    n = -5
    result = largest_divisor(n)
    assert result == -2

def test_small_positive_integer():
    n = 2
    result = largest_divisor(n)
    assert result == 1

def test_large_positive_integer():
    n = 100
    result = largest_divisor(n)
    assert result == 50

def test_zero():
    n = 0
    result = largest_divisor(n)
    assert result == 0

def test_divisors_not_found():
    n = 17
    result = largest_divisor(n)
    assert result is None

# Run all tests
if __name__ == "__main__":