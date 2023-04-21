def greatest_common_divisor(a: int, b: int) -> int:
    
    while b:
        a, b = b, a % b
    return a




def test():
    assert greatest_common_divisor(27, 6) == 3
    assert greatest_common_divisor(12, 6) == 6
