def is_simple_power(x, n):
    
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x) 


# test case

def test():
    assert is_simple_power(2, 3) == False
    assert is_simple_power(1, 2) == True
    assert is_simple_power(10, 3) == False
    assert is_simple_power(-1, 2) == False
