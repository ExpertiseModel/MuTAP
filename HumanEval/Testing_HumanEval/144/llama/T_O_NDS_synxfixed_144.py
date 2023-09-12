
def simplify(x, n):
    
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False


# test case
def test():
   
    # Test 1: Simple cases

    assert simplify("4/5", "3/4") == True

    # Test 2: Non-simple cases

    assert  simplify("10/20", "2/3") == False

    # Test 3: Negative numbers

    assert simplify("-4/5", "-3/4") == True

    # Test 4: Irrational numbers

    assert simplify("3.5/4", "2.5/3") == False

    # Test 5: Zero division