[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def truncate_number(number: float) -> float:
    
    return number % 1.0




# test case
def test():
    assert [/INST]  Certainly! Here are some test cases for the `truncate_number` function:
```
def test_truncate_positive_integer(self):
    self.assertEqual(truncate_number(5.0), 5.0)

def test_truncate_negative_integer(self):
    self.assertEqual(truncate_number(-5.0), -5.0)

def test_truncate_positive_ decimal(self):
    self.assertEqual(truncate_number(5.5), 5.0)

def test_truncate_negative_decimal(self):
    self.assertEqual(truncate_number(-5.5), -5.0)

def test_truncate_positive_float(self):
    self.assertEqual(truncate_number(5.2), 5.0)

def test_truncate_negative_float(self):
    self.assertEqual(truncate_number(-5.2), -5.0)

def test_edge_cases