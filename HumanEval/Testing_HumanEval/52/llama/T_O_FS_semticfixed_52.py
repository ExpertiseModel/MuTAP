def below_threshold(l: list, t: int):
    
    for e in l:
        if e >= t:
            return False
    return True




#</code>
#<test>

def test():
    assert below_threshold([], 5) == True

    assert below_threshold([5], 5) == False

    assert below_threshold([5, 10, 15, 20], 5) == False
    assert below_threshold([5, 10, 15, 20, 25], 5) == False
