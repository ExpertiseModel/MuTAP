def choose_num(x, y):
    
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1

def test():
    assert choose_num(3, 5) == -1
    assert choose_num(4, 7) == 4
    assert choose_num(4, 4) == -1
    assert choose_num(1, 5) == 5
    assert choose_num(2, 3) == 3
