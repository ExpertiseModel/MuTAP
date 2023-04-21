def below_threshold(l: list, t: int):
    
    for e in l:
        if e >= t:
            return False
    return True




def test():
    assert below_threshold([1.0, 2.0, 3.0, 4.0, 5.0], 3) == False
    assert below_threshold([1.0, 2.0, 3.0, 4.0, 5.0], 10) == True
    assert below_threshold([9.0, 1.0, 3.0, 4.0, 5.0], 3) == False
    assert below_threshold([1.0, 2.0, 10.0, 4.0, 5.0], 3) == False
