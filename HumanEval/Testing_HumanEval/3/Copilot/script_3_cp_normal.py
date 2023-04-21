from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    """
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False



 # generate test case for the function above

def test_below_zero():
    assert below_zero([1, 2, 3, -1, -2, -3]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3, -4]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3, -4, 1]) == True
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3, -4, 1, 2]) == False
    assert below_zero([1, 2, 3, -1, -2, -3, -4, 1, 2, 3, -1, -2, -3, -4, 1, 2, 3]) == False