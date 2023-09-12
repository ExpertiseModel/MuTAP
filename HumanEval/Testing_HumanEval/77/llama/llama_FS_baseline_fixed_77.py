def iscube(a):
    
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a


#</code>
#<test>

def test():
    assert iscube(1) == 1
    assert iscube(1.0) == 1
