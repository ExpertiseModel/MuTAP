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
# Test 1: Valid input
n = 10
assert largest_prime_factor(n) == 5

# Test 2: Non-prime input
n = 100
assert largest_prime_factor(n) == 10

# Test 3: Multiple prime factors
n = 24
assert largest_prime_factor(n) == 6

# Test 4: Input too large
n = 1000
assert largest_prime_factor(n) == 1000

# Test 5: Input too small
n = 2
assert largest_prime_factor(n) == 2
```
Explanation:

* Test 1: Here, we pass the input `n = 10` to the function, and check that the returned value `largest_prime_factor(n)` is equal to 5, which is the largest prime factor of 10.
* Test 2: In this test, we pass a non-prime value `n =