def is_prime(n):
    
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True


assert is_prime(11) == True
assert is_prime(2) == True
assert is_prime(12) == False
