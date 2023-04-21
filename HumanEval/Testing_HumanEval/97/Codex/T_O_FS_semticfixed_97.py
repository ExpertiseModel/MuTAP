def multiply(a, b):
    
    return abs(a % 10) * abs(b % 10)


def test():
    assert multiply(6,-3) == 42
    assert multiply(2, 3) == 6
    assert multiply(3, 4) == 12
