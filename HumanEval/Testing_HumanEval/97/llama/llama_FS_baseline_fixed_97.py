def multiply(a, b):
    
    return abs(a % 10) * abs(b % 10)


#</code>
#<test>

def test():
    assert multiply(3, 4) == 12
    assert multiply(0, 0) == 0
    assert multiply(3.5, 2.5) == 8.75
