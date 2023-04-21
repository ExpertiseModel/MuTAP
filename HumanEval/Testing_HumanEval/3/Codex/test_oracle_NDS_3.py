from typing import List


def below_zero(operations: List[int]) -> bool:
    
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False



def test():
    assert below_zero([1, 2, -1]) is True
    assert below_zero([1, -2, -1]) is True
    assert below_zero([1, 2, 3]) is False
    assert below_zero([1, -2, 3]) is False
    assert below_zero([-1, -2, -3]) is True
    assert below_zero([-1, -2, 3]) is True
    assert below_zero([-1, 2, -3]) is True


if __name__ == "__main__":
    test()