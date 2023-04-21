def greatest_common_divisor(a: int, b: int) -> int:
    
    while not b:
        a, b = b, a % b
    return a


