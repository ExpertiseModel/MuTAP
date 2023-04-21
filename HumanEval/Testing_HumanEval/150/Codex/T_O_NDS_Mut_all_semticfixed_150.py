def x_or_y(n, x, y):
    
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x




def test():
    assert x_or_y(1, 1, 0) == 0
    assert x_or_y(2, 0, 0) == 0
    assert x_or_y(3, 1, 0) == 1
    assert x_or_y(4, 1, 0) == 0
    assert x_or_y(5, 1, 0) == 1
    assert x_or_y(6, 0, 0) == 0
    assert x_or_y(7, 1, 0) == 1
    assert x_or_y(8, 1, 0) == 0
    assert x_or_y(9, 0, 0) == 0
    assert x_or_y(10, 0, 0) == 0
    assert x_or_y(11, 1, 0) == 1
    assert x_or_y(1, 1, 0) == 0
    assert x_or_y(2, 0, 0) == 0
    assert x_or_y(3, 1, 0) == 1
    assert x_or_y(4, 1, 0) == 0
    assert x_or_y(5, 1, 0) == 1
    assert x_or_y(6, 0, 0) == 0
    assert x_or_y(7, 1, 0) == 1
    assert x_or_y(8, 1, 0) == 0
    assert x_or_y(9, 0, 0) == 0
    assert x_or_y(10, 0, 0) == 0
    assert x_or_y(11, 1, 0) == 1
