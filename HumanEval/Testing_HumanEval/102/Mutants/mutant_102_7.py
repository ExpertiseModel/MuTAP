def choose_num(x, y):
    
    if x > y:
        return -1
    if not (y % 2 == 0):
        return y
    if x == y:
        return -1
    return y - 1
