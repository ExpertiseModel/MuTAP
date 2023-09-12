def is_simple_power(x, n):
    
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x) 


#</code>
#<test>

def test():
    assert is_simple_power(3, 3) == True
    assert is_simple_power(4, 2) == True
    assert is_simple_power(4, 3) == False
    assert is_simple_power(5, 2) == False
    assert is_simple_power(6, 2) == False

    assert is_simple_power(1, 1) == True
    assert is_simple_power(1, 2) == True
    assert is_simple_power(0, 1) == False
    assert is_simple_power(-1, 1) == False

    assert is_simple_power(-3, 3) == False
    assert is_simple_power(-4, 2) == False
    assert is_simple_power(-5, 2) == False
