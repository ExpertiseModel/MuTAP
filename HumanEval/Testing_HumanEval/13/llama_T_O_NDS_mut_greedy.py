def greatest_common_divisor(a: int, b: int) -> int:
    
    while b:
        a, b = b, a % b
    return a


assert greatest_common_divisor(6, 8) == 2
