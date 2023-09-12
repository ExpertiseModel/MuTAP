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
    assert [/INST]  Certainly! Here are some test cases for the `factorize` function:

Test 1: Basic functionality
-----------

def test_factorize_basic():
    assert factorize(3) == [3]
    assert factorize(4) == [2, 2]
    assert factorize(6) == [3, 2]
    assert factorize(8) == [2, 2, 2]
Test 2: Edge cases
-----------

def test_factorize_edge_cases():
    assert factorize(1) == []
    assert factorize(0) == []
    assert factorize(-1) == []
    assert factorize(9) == [3, 3]
Test 3: Large numbers
-----------

def test_factorize_large_numbers():
    assert factorize(1000) == [5, 10, 15, 25, 50, 75, 100, 150, 250]
Test 4: Negative numbers
-----------

def test_factor