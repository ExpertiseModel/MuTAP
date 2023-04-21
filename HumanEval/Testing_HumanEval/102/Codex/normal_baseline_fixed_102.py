def choose_num(x, y):
    
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1

def choose_num():
`python
def choose_num(x, y):
    if x > y:
        return -1
    if x == y:
        return -1

    if y % 2 == 0:
        return y
    else:
        return y - 1

# test case
