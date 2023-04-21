def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    """
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True


METADATA = {}



 # generate test case for the function above

def test_is_prime():
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(11) == True
    assert is_prime(12) == False
    assert is_prime(13) == True
    assert is_prime(14) == False
    assert is_prime(15) == False
   