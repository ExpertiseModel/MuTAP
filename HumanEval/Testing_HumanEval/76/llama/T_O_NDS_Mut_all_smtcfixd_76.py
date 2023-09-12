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
   
    assert is_simple_power(4, 2) == True
   
    assert is_simple_power(8, 3) == False

    assert is_simple_power(1, 2) == True
    
    assert is_simple_power(10, 3) == False

    assert is_simple_power(-1, 2) == False
    
    assert is_simple_power(0, 3) == False
    assert is_simple_power(2, 2) == True
    assert is_simple_power(-1, 2) == False
    assert is_simple_power(0, 2) == False
    # Test the edge case
    assert is_simple_power(-1, -1) == False
     # Test with n = 2
    assert is_simple_power(2, 2) == True
    # Test with n = 3
    assert is_simple_power(2, 3) == False
    # Test with n = 4
    assert is_simple_power(4, 3) == False
    # Test with n = 5
    assert is_simple_power(8, 3) == False
    # Test with n = 1
    assert is_simple_power(1, 2) == True
    # Test with n = -1
    assert is_simple_power(-1, 2) == False
    # Test with n = 0
    assert is_simple_power(0, 3) == False



