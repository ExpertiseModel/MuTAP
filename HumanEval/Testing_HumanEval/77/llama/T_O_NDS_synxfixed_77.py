def iscube(a):
    
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a


# test case
def test():
    
    # Test 1: positive input
    assert iscube(3) == True

    # Test 2: negative input

    assert  iscube(-4) == False

    # Test 3: input greater than 1
    assert  iscube(2 ** 3) == False

    # Test 4: input less than or equal to 1
    assert iscube(1) == True

    # Test 5: edge case

    assert not iscube(1.5) == False
