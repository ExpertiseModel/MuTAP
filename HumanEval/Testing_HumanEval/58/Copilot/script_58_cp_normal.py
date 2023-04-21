def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.

    """
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))


METADATA = {}



 # generate test case for the function above

def test_common():
    assert common([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert common([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5]
    assert common([1, 1, 3, 3, 5, 5], [1, 1, 3, 3, 5, 5]) == [1, 3, 5]
    assert common([1, 1, 3, 3, 5, 5, 7, 7], [1, 1, 3, 3, 5, 5, 7, 7]) == [1, 3, 5, 7]
    assert common([1, 1, 3, 3, 5, 5, 7, 7, 9, 9], [1, 1, 3, 3, 5, 5, 7, 7, 9, 9]) == [1, 3, 5, 7, 9]
    assert common([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11], [1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11]) == [1, 3, 5, 7, 9, 11]
    assert common([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13], [1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13]) == [1, 3, 5, 7, 9, 11, 13]