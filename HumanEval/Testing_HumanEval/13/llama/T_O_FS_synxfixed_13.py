def greatest_common_divisor(a: int, b: int) -> int:
    
    while b:
        a, b = b, a % b
    return a




def test():

    assert greatest_common_divisor(3, 4) == 2
    assert greatest_common_divisor(9, 10) == 1

    assert greatest_common_divisor(-3, 4) == -2
    assert greatest_common_divisor(-9, -10) == -1

    assert greatest_common_divisor(100, 200) == 50
    assert greatest_common_divisor(1000, 2000) == 500
