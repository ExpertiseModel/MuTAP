[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List


def factorize(n: int) -> List[int]:
    
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return fact




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `factorize` function:
```python
def test_factorize_single_digit_input():
    assert factorize(1) == [1]

def test_factorize_small_input():
    assert factorize(5) == [2, 2, 5]

def test_factorize_medium_input():
    assert factorize(42) == [2, 11, 4, 7]

def test_factorize_large_input():
    assert factorize(1000) == [1, 2, 5, 6, 10, 25, 50, 100, 250, 500, 1000]

def test_factorize_negative_input():
    assert factorize(-5) == [5, -1]

def test_factorize_zero_input():
    assert factorize(0) == [1]

def test_factorize_input_too_large():
    with pytest.raises(ValueError):