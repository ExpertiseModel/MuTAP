def common(l1: list, l2: list):
    
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))




def test():
    assert list(common([0, 4, 3, 2], [3, 2, 0])) == [0, 2, 3]
    assert list(common([0, 4, 3, 2], [3, 2, 0, 5])) == [0, 2, 3]
    assert list(common([1, 2, 3], [2, 3, 4])) == [2, 3]
