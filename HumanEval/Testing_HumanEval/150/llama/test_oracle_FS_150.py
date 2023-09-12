def x_or_y(n, x, y):
    
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x


#</original code>


def test():
   
    assert x_or_y(2, 2, 2) == 2
    assert x_or_y(2, 2, 3) == 2
    assert x_or_y(2, 3, 4) == 3
    assert x_or_y(3, 2, 4) == 3
    assert x_or_y(4, 2, 3) == 3