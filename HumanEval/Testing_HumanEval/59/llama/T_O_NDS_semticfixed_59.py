def largest_prime_factor(n: int):
    
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




# test case

def test():
    #test_small_numbers():
    assert largest_prime_factor(3) == 3
    #test_composite_numbers():
    assert largest_prime_factor(12) == 3
    #test_even_numbers():
    assert largest_prime_factor(10) == 5
    #test_larger_numbers():
    assert largest_prime_factor(100) == 5
    #test_edge_cases():
    assert largest_prime_factor(-5) == 1
    #test_NaN():
    assert largest_prime_factor(None) == None    #test_inf():
    assert largest_prime_factor(1000) == 5
