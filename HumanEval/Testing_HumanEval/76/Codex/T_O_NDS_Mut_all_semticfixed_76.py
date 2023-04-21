def is_simple_power(x, n):
    
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x) 




def test():
    assert is_simple_power(4, 2) == True
    assert is_simple_power(4, 3) == False
    assert is_simple_power(4, 4) == True
    assert is_simple_power(4, 5) == False
    assert is_simple_power(4, 6) == False
    assert is_simple_power(4, 7) == False
    assert is_simple_power(4, 8) == False
    assert is_simple_power(4, 9) == False
    assert is_simple_power(4, 10) == False
    assert is_simple_power(4, 11) == False
    assert is_simple_power(4, 12) == False
    assert is_simple_power(4, 13) == False
    assert is_simple_power(4, 4) == True
    assert is_simple_power(4, 1) == False
    assert is_simple_power(4, 2) == True
    assert is_simple_power(4, 3) == False
    assert is_simple_power(4, 4) == True
    assert is_simple_power(4, 5) == False
    assert is_simple_power(4, 6) == False
    assert is_simple_power(4, 7) == False
    assert is_simple_power(4, 8) == False
    assert is_simple_power(4, 9) == False
    assert is_simple_power(4, 10) == False
    assert is_simple_power(4, 11) == False
    assert is_simple_power(4, 12) == False
    assert is_simple_power(4, 13) == False
