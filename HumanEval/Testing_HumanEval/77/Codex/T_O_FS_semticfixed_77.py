def iscube(a):
    
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a


def test():
    assert iscube(1) == True
    assert iscube(2) == False
    assert iscube(25) == False
    assert iscube(27) == True
    assert iscube(823625) == False
