def is_simple_power(x, n):
    
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x) 


def test():
    assert is_simple_power(4, 2) == True
    assert is_simple_power(32, 4) == False
    assert is_simple_power(9, 2) == False
    assert is_simple_power(81, 3) == True
    assert is_simple_power(225, 4) == False
