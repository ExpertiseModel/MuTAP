def common(l1: list, l2: list):
    
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))



def test():
    assert common([2, 3, 6], [1, 2, 3, 4, 6]) == [2, 3, 6]
    assert common([1], [1]) == [1]
    assert common([1, 2, 3], [3, 4, 5]) == [3]

test()



