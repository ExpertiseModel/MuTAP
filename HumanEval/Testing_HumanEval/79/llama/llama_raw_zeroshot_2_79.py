[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def decimal_to_binary(decimal):
    
    return "db" + bin(decimal)[2:] + "db"


# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `decimal_to_binary` function using the `unittest` module in Python:
```
import unittest

class TestDecimalToBinary(unittest.TestCase):
    def test_positive_input(self):
        self.assertEqual(decimal_to_binary(123), 'db11111')
    def test_negative_input(self):
        self.assertEqual(decimal_to_binary(-123), 'db11110')
    def test_zero_input(self):
        self.assertEqual(decimal_to_binary(0), 'db00000')
if __name__ == '__main__':
    unittest.main()
```
Explanation:

* In the `test_positive_input` method, we pass a positive integer `decimal` to the `decimal_to_binary` function and assert that the result is `"db11111"`.
* In the `test_negative_input` method, we pass a negative integer `dec