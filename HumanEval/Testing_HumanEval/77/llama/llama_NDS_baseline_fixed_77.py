def iscube(a):
    
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a


# test case

def test():
    assert  iscube(-4) == False
    assert iscube(1) == True
