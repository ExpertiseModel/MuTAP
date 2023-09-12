[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    
    return [x for x in values if isinstance(x, int)]




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `filter_integers` function using Python's built-in `unittest` module:
```python
import unittest

class TestFilterIntegers(unittest.TestCase):
    def test_filter_empty_list(self):
        values = []
        result = filter_integers(values)
        self.assertEqual(result, [])
    
    def test_filter_single_integer(self):
        values = [1, "hello", 42, "world"]
        result = filter_integers(values)
        self.assertEqual(result, [42])
    def test_filter_mixed_types(self):
        values = [1, "hello", 42, "world", 0.5, "foo"]
        result = filter_integers(values)
        self.assertEqual(result, [42, 0.5])
    def test_filter_none(self):
        values = [1, None, "hello", 42, "world"]
        result = filter_integers(values