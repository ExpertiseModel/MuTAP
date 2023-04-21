def is_prime(n):
    
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True




def test():
    assert is_prime(11) == True
    assert is_prime(12) == False
    assert is_prime(13) == True
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(22) == False
    assert is_prime(24) == False
    assert is_prime(25) == False
    assert is_prime(26) == False
    assert is_prime(28) == False
    assert is_prime(100) == False
    assert is_prime(200) == False
    assert is_prime(300) == False
