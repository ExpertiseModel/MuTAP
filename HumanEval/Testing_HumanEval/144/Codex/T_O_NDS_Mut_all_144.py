def simplify(x, n):
    
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False



def test():

    assert simplify("123/456", "321/654") == False
    assert simplify("123/456", "12/15") == False
    assert simplify("123/456", "9/12") == False
    assert simplify("123/456", "7/12") == False
    assert simplify("123/456", "7/15") == False
    assert simplify("123/456", "321/654") == False
    assert simplify("123/456", "12/15") == False
    assert simplify("123/456", "9/12") == False
    assert simplify("123/456", "7/12") == False
    assert simplify("123/456", "7/15") == False

    assert simplify("123/456", "321/654") == False
    assert simplify("123/456", "12/15") == False
    assert simplify("123/456", "9/12") == False
    assert simplify("123/456", "7/12") == False
    assert simplify("123/456", "7/15") == False

    assert simplify("123456789/123456789", "1/2") == False
    assert simplify("123456789/123456789", "123/456") == False
    assert simplify("987/654", "321/654") == False
    assert simplify("987/654", "12/15") == False
    assert simplify("987/654", "9/12") == False
    assert simplify("987/654", "7/12") == False
    assert simplify("987/654", "7/15") == False

    assert simplify("123/456", "321/654") == False
    assert simplify("123/456", "12/15") == False
    assert simplify("123/456", "9/12") == False
    assert simplify("123/456", "7/12") == False
    assert simplify("123/456", "7/15") == False

    assert simplify("123/456", "321/654") == False
    assert simplify("123/456", "12/15") == False
    assert simplify("123/456", "9/12") == False
    assert simplify("123/456", "7/12") == False
    assert simplify("123/456", "7/15") == False

