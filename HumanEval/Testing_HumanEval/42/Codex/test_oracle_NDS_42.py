def incr_list(l: list):
    
    return [(e + 1) for e in l]



def test():
    assert incr_list([2, 3, 4]) == [3, 4, 5]
