def incr_list(l: list):
    
    return [(e + 1) for e in l]




def test():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([-1, 0, 1]) == [0, 1, 2]
