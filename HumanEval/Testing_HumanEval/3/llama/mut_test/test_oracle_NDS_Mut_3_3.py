[INST] <<SYS>>
#You are a python coding assistant. Always answer with python code.
<</SYS>>

#Generate test cases for the following function:```python
 from typing import List


def below_zero(operations: List[int]) -> bool:
    
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False




# test case
import unittest

``` [/INST] ```python
 def test():
    
    #test_negative_operations
   assert below_zero([1, -2, -3, 4, -5]) is True
   #test_positive_operations
   assert below_zero([1, 2, 3, 4, 5]) is False
   #test_zero_operations
   assert below_zero([0, 0, 0, 0, 0]) is False


 ```  [INST] #The test cases that you generated in test(), cannot detect the mutation in the following code snippet.
```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    
    balance = 0

    for op in operations:
        balance += op
        if balance <= 0:
            return True

    return False





```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST]  Ah, I see. In that case, you can modify the test case to check for the potential mutation by adding a new test case that verifies the expected behavior when the `balance` variable is initialized to a non-zero value. Here's an updated test case that includes this test:
```python
# test case
def test():
    # test negative operations
    assert below_zero([1, -2, -3, 4, -5]) is True
    # test positive operations
    assert below_zero([1, 2, 3, 4, 5]) is False
    # test zero operations
    assert below_zero([0, 0, 0, 0, 0]) is False
    # test mutation
    assert below_zero([1, 2, 3, 4, 5], balance=5) is False

```
In this updated test case, we add a new test (`test_mutation`) that passes a list of integers `operations` to the `below_zero` function with a non-zero initial value for the `balance` variable (in this case, 5). We