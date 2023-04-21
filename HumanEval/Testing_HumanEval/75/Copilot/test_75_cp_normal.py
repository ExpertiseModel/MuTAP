from script_75_cp_normal import is_multiply_prime

def test_is_multiply_prime():
    assert is_multiply_prime(2) == False
    assert is_multiply_prime(3) == False
    assert is_multiply_prime(4) == False
    assert is_multiply_prime(5) == False
    assert is_multiply_prime(6) == True
    assert is_multiply_prime(7) == False
    assert is_multiply_prime(8) == False
    assert is_multiply_prime(9) == False
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(11) == False
    assert is_multiply_prime(12) == True
    assert is_multiply_prime(13) == False
    assert is_multiply_prime(14) == False
    assert is_multiply_prime(15) == True
    assert is_multiply_prime(16) == False
    assert is_multiply_prime(17) == False
    