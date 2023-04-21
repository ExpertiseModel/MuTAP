def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.
    """
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1

 # generate test case for the function above
def test_choose_num():
    assert choose_num(1, 2) == 2
    assert choose_num(2, 2) == -1
    assert choose_num(2, 3) == 2
    assert choose_num(2, 4) == 4
    assert choose_num(2, 5) == 4
    assert choose_num(2, 6) == 6
