def multiply(a, b):
    
    return abs(a % 10) * abs(b % 10)


def test():
    assert multiply(3, 3) == 9
    assert multiply(2, 3) == 6
    assert multiply(0, 3) == 0
    assert multiply(0, 2) == 0
    assert multiply(2, 3) == 6
    assert multiply(2, 3) == 6
    assert multiply(3, 4) == 12
    assert multiply(3, 5) == 15
    assert multiply(3,6) == 18
