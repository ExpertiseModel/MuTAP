def iscube(a):
    
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a


#</code>
#<test>
def test():
    
    assert iscube(1) == 1
    assert iscube(2) == 8
    assert iscube(3) == 27
    assert iscube(-1) == -1
    assert iscube(0) == 0
    assert iscube(4) == 16
    assert iscube(-4) == -16
    assert iscube(100) == 10000
#</test>

    assert iscube(3.0) == 27
    assert iscube(-3.0) == -27
    assert iscube(4.0) == 16
    assert iscube(-4.0) == -16
    assert iscube(0.0) == 0
    assert iscube(1.0) == 1

#</test>

#<code>

def test():
    a