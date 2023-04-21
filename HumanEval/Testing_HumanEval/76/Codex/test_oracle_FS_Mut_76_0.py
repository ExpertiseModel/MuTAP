def is_simple_power(x, n):
    
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x) 



def test():
    assert is_simple_power(4, 2) == True
    assert is_simple_power(25, 3) == False
    assert is_simple_power(32, 4) == False
    assert is_simple_power(9, 2) == False
    assert is_simple_power(81, 3) == True
    assert is_simple_power(225, 4) == False
    assert is_simple_power(1, 4) == True
    assert is_simple_power(2, 2) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(3, 2) == False
    assert is_simple_power(3, 1) == False
    assert is_simple_power(5, 3) == False
    assert is_simple_power(99999, 2) == True
    assert is_