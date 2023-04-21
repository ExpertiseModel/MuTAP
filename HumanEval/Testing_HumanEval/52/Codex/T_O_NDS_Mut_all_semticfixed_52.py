def below_threshold(l: list, t: int):
    
    for e in l:
        if e >= t:
            return False
    return True






def test():
    assert below_threshold([0, 2, 3], 2) == False
    assert below_threshold([1, 2, 3], 2) == False
    assert below_threshold([2, 2, 3], 2) == False
    assert below_threshold([2, 3, 3], 2) == False
    assert below_threshold([1, 2, 3], 2) == False
    assert below_threshold([1, 2, 3], 3) == False
    assert below_threshold([2, 2, 3], 2) == False
    assert below_threshold([2, 3, 3], 2) == False
    assert below_threshold([2, 2, 2], 2) == False
    assert below_threshold([3, 3, 3], 2) == False
    assert below_threshold([3, 3, 3], 3) == False
