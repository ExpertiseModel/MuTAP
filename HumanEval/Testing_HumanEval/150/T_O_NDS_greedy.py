def x_or_y(n, x, y):
    
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x
assert x_or_y(3, 1, 0) == 1
assert x_or_y(4, 1, 0) == 0
