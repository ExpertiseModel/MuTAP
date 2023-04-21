def choose_num(x, y):
    
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1




def test():
    assert choose_num(3, 5) == 4
    assert choose_num(4, 7) == 6
    assert choose_num(4, 4) == 4
    assert choose_num(1, 5) == 4
    assert choose_num(2, 3) == 2
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(12, 12) == 12
