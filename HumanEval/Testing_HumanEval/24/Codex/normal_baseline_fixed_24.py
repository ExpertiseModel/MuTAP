def largest_divisor(n: int) -> int:
    
    for i in reversed(range(n)):
        if n % i == 0:
            return i




def test():
    assert largest_divisor(4) == 2, "2"
    assert largest_divisor(5) == 1, "5"
    assert largest_divisor(6) == 3, "3"
    assert largest_divisor(9) == 3, "3"
