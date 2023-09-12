def add(x: int, y: int):
    
    return x + y




# test case
def test():
    assert add(2, 3) == 5
    assert add(3, 2) == 5
    assert add(5, 0) == 5
    assert add(0, 5) == 0
    assert add(10, 10) == 20
    assert add(-3, -2) == -5
    assert add(-2, -3) == -5
    assert add(10, -2) == 8
    assert add(-10, 10) == -0
    assert add(0, 0) == 0
    assert add(2, 3) == 5
    assert add(3, 2) == 5
    assert add(5, 0) == 5