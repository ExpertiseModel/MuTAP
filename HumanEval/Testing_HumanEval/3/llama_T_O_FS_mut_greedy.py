from typing import List


def below_zero(operations: List[int]) -> bool:
    
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False


assert below_zero([1, 2, 3, 4, 5], balance=5) is False
