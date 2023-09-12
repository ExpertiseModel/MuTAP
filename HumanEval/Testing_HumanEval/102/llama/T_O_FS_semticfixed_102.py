def choose_num(x, y):
    
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1


#</code>
#<test>

def test():
    assert choose_num(3, 2) == -1
    assert choose_num(2, 1) == -1
    assert choose_num(3, 4) == 4
    assert choose_num(4, 2) == -1
    assert choose_num(2, 3) == 2
    assert choose_num(5, 3) == -1
    assert choose_num(6, 2) == -1
    assert choose_num(7, 3) == -1
