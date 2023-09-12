def iscube(a):
    
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a


#</code>
#<test>

def test():
    assert iscube(1) == 1
    assert iscube(2) == False
    assert iscube(3) == False
    assert iscube(-1) == True
    assert iscube(0) == True
    assert iscube(4) == False
    assert iscube(-4) == False
    assert iscube(100) == False
#</test>

    assert iscube(3.0) == False
    assert iscube(-3.0) == False
    assert iscube(4.0) == False
    assert iscube(-4.0) == False
    assert iscube(0.0) == True
    assert iscube(1.0) == 1

#</test>

#<code>


