def incr_list(l: list):
    """Return list with elements incremented by 1.
    """
    return [(e + 1) for e in l]


METADATA = {}



 # generate test case for the function above

def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([-1, 0, 1]) == [0, 1, 2]
    assert incr_list([]) == []
    assert incr_list([1]) == [2]
    assert incr_list([1, 2, 3, 4]) == [2, 3, 4, 5]
    assert incr_list([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 6]
    assert incr_list([1, 2, 3, 4, 5, 6]) == [2, 3, 4, 5, 6, 7]