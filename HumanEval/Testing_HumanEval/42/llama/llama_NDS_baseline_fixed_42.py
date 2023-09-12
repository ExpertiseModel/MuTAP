def incr_list(l: list):
    
    return [(e + 1) for e in l]




# test case

def test():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([1, 2, 3, 4, 5, 6]) == [2, 3, 4, 5, 6, 7]
    assert incr_list([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 6]
    assert incr_list([1.0, 2.0, 3.0, 4.0, 5.0]) == [2.0, 3.0, 4.0, 5.0, 6.0]
