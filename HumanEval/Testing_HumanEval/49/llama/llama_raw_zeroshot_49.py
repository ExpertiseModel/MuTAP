[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def modp(n: int, p: int):
    
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret




# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `modp` function using the `unittest` module in Python:
```
import unittest

class TestModp(unittest.TestCase):
    def test_return_value(self):
        self.assertEqual(modp(10, 7), 3)
    def test_large_n(self):
        self.assertEqual(modp(1000, 11), 233)
    def test_small_p(self):
        self.assertEqual(modp(10, 3), 1)
    def test_high_p(self):
        self.assertEqual(modp(10, 10000), 0)
if __name__ == '__main__':
    unittest.main()
```
Explanation:

* In the `test_return_value` method, we call the `modp` function with `n=10` and `p=7` and check that the result is `3`.
* In the `test_large_n` method,