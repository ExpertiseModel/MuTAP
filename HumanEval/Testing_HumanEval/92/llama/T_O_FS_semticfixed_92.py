def any_int(x, y, z):
  
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False


#</code>
#<test>

def test():
    assert any_int(1, 2, 3) is True

#</testCase>

    assert any_int(1, 2.5, 3) is False

#</testCase>

    assert any_int(1, 2, 3) is True
    assert any_int(1, 2, 4) is False

#
    assert any_int(1, 2, 3) is True
    assert any_int(2, 3, 4) is False


    assert any_int(1, 2, 3) is True
    assert any_int(1, 3, 4) is True
