def largest_divisor(n: int) -> int:
    
    for i in reversed(range(n)):
        if n % i == 0:
            return i




# test case
def test():
   
    assert largest_divisor(1) == 1
    assert largest_divisor(2) == 2
    assert largest_divisor(3) == 3

    assert largest_divisor(n) == n


    assert largest_divisor(100) == 100

    assert largest_divisor(-10) == 0


    assert largest_divisor(0) == 1

    assert largest_divisor(float('inf')) == float('inf')
