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

    assert below_zero([1, -2, -3, 4, 5]) is False

    assert below_zero([1, 2, 3, 4, 5]) is False

    assert below_zero([1, 2, 3, 4, 5]) is False
    # test negative operations with changed logic
    assert below_zero([-1, -2, -3, -4, -5]) is False
    # test positive operations with changed logic
    assert below_zero([1, 2, 3, 4, -5]) is True

    assert below_zero([1, -2, -3, 4, -5]) is True
    # test positive operations
    assert below_zero([1, 2, 3, 4, 5]) is False
    # test zero operations
    assert below_zero([0, 0, 0, 0, 0]) is False
    # test mutation
    assert below_zero([1, 2, 3, 4, 5], balance=5) is False



