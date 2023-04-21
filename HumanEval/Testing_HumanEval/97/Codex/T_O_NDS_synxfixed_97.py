def multiply(a, b):
    
    return abs(a % 10) * abs(b % 10)

def test():
    assert multiply(3, 3) == 9
    assert multiply(2, 3) == 6
    assert multiply(0, 3) == 0
    assert multiply(0, 2) == 0
    assert multiply(2, 3) == 6
    assert multiply(2, 3) == 6
    assert multiply(9876, 789) == 973714
    assert multiply(10, 10) == 100
    assert multiply(3, 10) == 30
    assert multiply(1, 1000) == 1000
    assert multiply(3, 4) == 12
    assert multiply(3, 5) == 15
    assert multiply(3,6) == 18
#####
def multiply(a, b):
    is_neg = False
    if a < 0:
        is_neg = not is_neg
    if b < 0:
        is_neg = not is_neg
