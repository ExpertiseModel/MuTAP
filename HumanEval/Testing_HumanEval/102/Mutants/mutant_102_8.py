def choose_num(x, y):
    
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if not (x == y):
        return -1
    return y - 1
