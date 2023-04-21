def largest_divisor(n: int) -> int:
    
    for i in reversed(range(n)):
        if n % i == 0:
            return i




def test():
    assert largest_divisor(10) == 5
    assert largest_divisor(9) == 3
