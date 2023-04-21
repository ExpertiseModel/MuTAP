from typing import List


def below_zero(operations: List[int]) -> bool:
    
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False





def test():
    #assert below_zero([10, -11, -10, -5]) == True

    #assert below_zero([10, -11, -10, -5, 0]) == True
    #assert below_zero([10, -11, -10, -5, 9]) == True
    #assert below_zero([10, -11, -10, -5, -2]) == True
    #assert below_zero([10, -11, -10, -5, -9]) == True
    #assert below_zero([10, -11, -10, -5, -9, -3]) == True
    #assert below_zero([10, -11, -10, -5, -9, -3, 7]) == True
    #assert below_zero([10, -11, -10, -5, -9, -3, -1]) == True