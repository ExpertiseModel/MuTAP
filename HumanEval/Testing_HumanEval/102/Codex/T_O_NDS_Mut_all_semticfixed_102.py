def choose_num(x, y):
    
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1





def test():
    assert choose_num(5,9) == 8
    assert choose_num(6,10) == 10
    assert choose_num(6,11) == 10
    assert choose_num(8,12) == 12
    assert choose_num(2, 3) == 2
    assert choose_num(2, 4) == 4
    assert choose_num(0, 1) == 0
    assert choose_num(0, 0) == 0
