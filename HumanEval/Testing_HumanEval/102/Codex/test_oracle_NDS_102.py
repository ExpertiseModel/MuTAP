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
def test():
     assert choose_num(5,9) == 7
     assert choose_num(6,10) == 8
     assert choose_num(6,11) == -1
     assert choose_num(8,12) == -1
