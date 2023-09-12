def largest_divisor(n: int) -> int:
    for i in reversed(range(n)):
        if n % i == 0:
            return i


def test():
    assert largest_divisor(4) == 2
    assert largest_divisor(6) == 3
    assert largest_divisor(7) == 1
