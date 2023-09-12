def choose_num(x, y):
    
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1


# test case

def test():
    # Test with positive integers
    assert choose_num(3, 4) == 4
    assert choose_num(7, 3) == -1
    # Test with non-integer arguments
    # Test edge cases
    assert choose_num(0, 0) == 0
    assert choose_num(1, 1) == -1
    assert choose_num(-1, -1) == -1
    # Test with larger integers
    assert choose_num(10, 5) == -1
    assert choose_num(100, 50) == -1
    # Test with odd and even numbers
    assert choose_num(3, 5) == 4
    assert choose_num
