def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    '''
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a

 # generate test case for the function above

def test_iscube():
    assert iscube(27) == True
    assert iscube(64) == False
    assert iscube(125) == True
    assert iscube(216) == True
    assert iscube(343) == True
    assert iscube(512) == False
    assert iscube(729) == True
    assert iscube(1000) == False
    assert iscube(1331) == False
    assert iscube(1728) == True
    assert iscube(2197) == True
    assert iscube(2744) == False
    assert iscube(3375) == True
    assert iscube(4096) == False
    