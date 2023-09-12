def incr_list(l: list):
    
    return [(e + 1) for e in l]




#</code>
#<test>
def test():
    assert incr_list([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 6]
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([4, 5, 6]) == [5, 6, 7]
    assert incr_list([7, 8, 9]) == [8, 9, 10]
    assert incr_list([]) == []