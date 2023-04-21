def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    """
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x) 

 # generate test case for the function above

def test_is_simple_power():
    assert is_simple_power(1, 1) == True
    assert is_simple_power(2, 1) == False
    assert is_simple_power(2, 2) == True
    assert is_simple_power(4, 2) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(9, 2) == False
    assert is_simple_power(9, 3) == True
    assert is_simple_power(27, 3) == True
    assert is_simple_power(81, 3) == True
    assert is_simple_power(243, 3) == True
    assert is_simple_power(256, 3) == False
    assert is_simple_power(256, 4) == True
    assert is_simple_power(625, 5) == True
    assert is_simple_power(625, 6) == False
    assert is_simple_power(4096, 4) == True
    