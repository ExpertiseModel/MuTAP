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
    assert [/INST]  Sure! Here are some test cases for the `is_prime` function using the `unittest` module in Python:
```python
import unittest

class TestIsPrime(unittest.TestCase):
    def test_positive_number(self):
        n = 10
        result = is_prime(n)
        self.assertTrue(result)

    def test_negative_number(self):
        n = -5
        result = is_prime(n)
        self.assertFalse(result)

    def test_small_number(self):
        n = 2
        result = is_prime(n)
        self.assertTrue(result)

    def test_big_number(self):
        n = 100
        result = is_prime(n)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```
Explanation:

* In the `test_positive_number` method, we call the `is_prime` function with a positive number (10),