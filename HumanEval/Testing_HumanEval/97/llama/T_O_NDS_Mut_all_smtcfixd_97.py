
def multiply(a, b):
    
    return abs(a % 10) * abs(b % 10)


# test case


def test():
    assert multiply(10, 10) == 0


    assert multiply(0, 10) == 0


    assert multiply(-10, 10) == 0


    assert multiply(10, -10) == 0


    assert multiply(0, -10) == 0


    assert multiply(-10, 10) == 0

    assert multiply(0, 0) == 0
    assert multiply(5, 10) == multiply(5, 10 * 10)
    assert multiply(10, 10) == 0

    assert multiply(0, 10) == 0

    assert multiply(-10, 10) == 0

    assert multiply(10, -10) == 0

    assert multiply(0, -10) == 0

    assert multiply(-10, 0) == 0

