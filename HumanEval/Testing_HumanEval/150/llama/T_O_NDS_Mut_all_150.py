def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x


# test case

def test():
    assert x_or_y(7, 34, 12) == 34

    assert x_or_y(15, 8, 5) == 5


    assert x_or_y(1, 5, 9) == 9


    assert x_or_y(30, 20, 10) == 10

    assert x_or_y(-7, -34, -12) == -34
    assert x_or_y(100, 50, 20) == 20
    assert x_or_y(7, 34, 12) == 34

    # Test that the function returns the correct value for a composite number
    assert x_or_y(15, 8, 5) == 5

    # Test that the function returns None for a non-prime number
    assert x_or_y(4, 2, 3) == None
