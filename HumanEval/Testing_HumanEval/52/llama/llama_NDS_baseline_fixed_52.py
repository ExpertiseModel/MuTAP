def below_threshold(l: list, t: int):
    
    for e in l:
        if e >= t:
            return False
    return True




# test case

def test():
    assert below_threshold([1, 2, 3], 1) == False
    assert below_threshold
