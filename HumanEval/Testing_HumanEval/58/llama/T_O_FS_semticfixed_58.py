def common(l1: list, l2: list):
    
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))






def test():
    assert common([], []) == []
# Test 2

    assert common([1], [1]) == [1]
# Test 3
    assert common([1, 2], [2, 1]) == [1, 2]
# Test 4
    assert common([1, 2, 3], [2, 3, 1]) == [1, 2, 3]
# Test 5
    assert common([1, 2, 2], [2, 2, 1]) == [1, 2]
# Test 6
    assert common([1, 2, 3], [4, 5, 6]) == []
