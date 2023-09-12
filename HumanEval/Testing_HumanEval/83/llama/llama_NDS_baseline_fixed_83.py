def starts_one_ends(n):
    
    if n == 1: 
        return 1
    return 18 * (10 ** (n - 2))


# test case

def test():
    assert starts_one_ends(1) == 1
    assert starts_one_ends(1) == 1
