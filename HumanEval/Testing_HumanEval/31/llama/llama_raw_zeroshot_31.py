[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def is_prime(n):
    
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True




# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `is_prime` function:
```
def test():
    # Test with small inputs
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    # Test with composites
    assert not is_prime(4)
    assert not is_prime(7)
    # Test with edge cases
    assert is_prime(1)
    assert is_prime(10)
    # Test with large inputs
    assert not is_prime(100)
    assert not is_prime(1000)

def test_composites():
    # Test with known composites
    assert not is_prime(6)
    assert not is_prime(10)
    assert not is_prime(12)
    assert not is_prime(24)

def test_edge_cases():
    # Test with small inputs near the limit
    assert is_prime(1)
    assert is_prime(10)
    assert not is_prime(100000000