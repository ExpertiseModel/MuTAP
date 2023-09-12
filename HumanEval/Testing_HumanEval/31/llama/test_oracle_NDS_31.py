def is_prime(n):
    
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True




# test case
def test():
    # Test with small inputs
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    # Test with composites
    assert is_prime(4) == False
    assert is_prime(7) == False
    # Test with edge cases
    assert is_prime(1) == True
    assert is_prime(10) == True
    # Test with large inputs
    assert is_prime(100) == False
    assert is_prime(1000) == False

    # Test with known composites
    assert is_prime(6) == False
    assert is_prime(10) == False
    assert is_prime(12) == False
    assert is_prime(24) == False
  
    # Test with small inputs near the limit
    assert is_prime(1) == True
    assert is_prime(10) == True
    assert not is_prime(100000000