def largest_divisor(n: int) -> int:
    
    for i in reversed(range(n)):
        if n % i == 0:
            return i




# test case

def test():
    assert largest_divisor(1) == 1    
    assert largest_divisor(2) == 1
    assert largest_divisor(3) == 1

    assert largest_divisor(100) == 50

    assert largest_divisor(-10) == None


    assert largest_divisor(0) == None

    assert largest_divisor(float('inf')) == float('inf')
