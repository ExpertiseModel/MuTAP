def is_prime(n):
    
    if not (n < 2):
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True


