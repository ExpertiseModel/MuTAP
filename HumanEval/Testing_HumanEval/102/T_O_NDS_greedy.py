def choose_num(x, y):
    
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1
assert choose_num(5,9) == 8
assert choose_num(6,10) == 10
