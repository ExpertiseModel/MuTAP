def simplify(x, n):
    
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False


def test():
    assert simplify("3/4", "2/3") == False
    assert simplify("3/4", "1/3") == False
    assert simplify("3/4", "1/6") == False

    assert simplify("3/4", "2/6") == False
    assert simplify("2/3", "1/6") == False
