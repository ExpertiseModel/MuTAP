[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def largest_prime_factor(n: int):
    
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `largest_prime_factor` function:
```
def test_small_numbers():
    assert largest_prime_factor(3) == 3
def test_composite_numbers():
    assert largest_prime_factor(12) == 2
def test_even_numbers():
    assert largest_prime_factor(10) == 2
def test_larger_numbers():
    assert largest_prime_factor(100) == 4
def test_edge_cases():
    assert largest_prime_factor(-5) == -1
def test_NaN():
    assert largest_prime_factor(None) == None
def test_inf():
    assert largest_prime_factor(1000) == 15
```
Here's a brief explanation of each test case:
* `test_small_numbers`: Tests the function on small positive integers, ensuring that it returns the correct largest prime factor.
* `test_composite_numbers`: Tests the function on composite numbers (i.e., numbers that are divisible by another prime number except