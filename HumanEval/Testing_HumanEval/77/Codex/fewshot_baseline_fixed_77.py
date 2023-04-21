def iscube(a):
    
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a


def test():
    assert iscube(1) == True
    assert iscube(2) == False
