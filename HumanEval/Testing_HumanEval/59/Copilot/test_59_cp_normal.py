from script_59_cp_normal import largest_prime_factor

def test_largest_prime_factor():
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(3) == 3
    assert largest_prime_factor(4) == 2
    assert largest_prime_factor(5) == 5
    assert largest_prime_factor(6) == 3
    assert largest_prime_factor(7) == 7
    assert largest_prime_factor(8) == 2
    assert largest_prime_factor(9) == 3
    assert largest_prime_factor(10) == 5
    assert largest_prime_factor(11) == 11
    assert largest_prime_factor(12) == 3
    assert largest_prime_factor(13) == 13
    assert largest_prime_factor(14) == 7
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(16) == 2
