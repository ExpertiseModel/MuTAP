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
    assert [/INST]  Great! Here are some test cases for the `below_zero` function:
```python
def test():
    # Test with empty list
    assert below_zero([])

def test():
    # Test with list of positive numbers
    operations = [1, 2, 3, 4, 5]
    assert not below_zero(operations)

def test():
    # Test with list of negative numbers
    operations = [-1, -2, -3, -4, -5]
    assert below_zero(operations)

def test():
    # Test with list of mixed numbers
    operations = [1, -2, 3, 4, -5]
    assert not below_zero(operations)

def test():
    # Test with list of very large numbers
    operations = [100, 200, 300, 400, 500]
    assert below_zero(operations)
```
Let me explain what each test case is doing:
* In the first test case, we call the `below_zero` function with an