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
def test():
   #test_negative_operations
   assert below_zero([1, -2, -3, 4, -5]) is True
   #test_positive_operations
   assert below_zero([1, 2, 3, 4, 5]) is False
   #test_zero_operations
   assert below_zero([0, 0, 0, 0, 0]) is False

