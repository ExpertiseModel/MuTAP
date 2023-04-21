def choose_num(x, y):
    
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1




def test():
    assert choose_num(2, 3) == 3
    assert choose_num(2, 4) == 3
    assert choose_num(0, 1) == -1
    assert choose_num(0, 0) == -1
