def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.

    """
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest


METADATA = {}



 # generate test case for the function above

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
