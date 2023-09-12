[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List


def below_zero(operations: List[int]) -> bool:
    
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False




# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `below_zero` function using the `unittest` module in Python:
```
import unittest

class TestBelowZero(unittest.TestCase):
    def test_negative_operations(self):
        operations = [1, -2, -3, 4, -5]
        result = below_zero(operations)
        self.assertTrue(result)

    def test_positive_operations(self):
        operations = [1, 2, 3, 4, 5]
        result = below_zero(operations)
        self.assertFalse(result)

    def test_zero_operations(self):
        operations = [0, 0, 0, 0, 0]
        result = below_zero(operations)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
```
In this example, we define three test methods: `test_negative_operations`, `test_positive_operations`, and `test_zero