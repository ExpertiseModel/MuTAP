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
    assert choose_num(3, 4) == 4
    assert choose_num(7, 3) == -1
    assert choose_num(0, 0) == 0
    assert choose_num(-1, -1) == -1
    assert choose_num
