def simplify(x, n):
    
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False



def test():
    
    assert simplify(2, 3) == False
    assert simplify(3, 2) == False
    assert simplify(4, 2) == True
    assert simplify(5, 3) == True
    assert simplify("4/8", "2/4") == True
    assert simplify("4/2", "2/2") == True
    assert simplify("4/2", "2/4") == False
    