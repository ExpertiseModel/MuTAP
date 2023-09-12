[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def total_match(lst1, lst2):
   
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2


# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `total_match` function in Python using the `unittest` module:
```
import unittest

class TestTotalMatch(unittest.TestCase):
    def test_good_input(self):
        lst1 = ['hello', 'world']
        lst2 = ['world', 'hello']
        self.assertEqual(total_match(lst1, lst2), lst1)
    def test_bad_input1(self):
        lst1 = ['hello', 'world']
        lst2 = ['apple', 'banana']
        self.assertNotEqual(total_match(lst1, lst2), lst2)
    def test_bad_input2(self):
        lst1 = ['hello', 'world']
        lst2 = ['hello', 'world']
        self.assertEqual(total_match(lst1, lst2), lst1)
if __name__ == '__main__':
    unittest.main()

```
Here's how the test cases work:

* In `test_good_input`, we pass two lists `lst