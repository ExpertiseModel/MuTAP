def largest_divisor(n: int) -> int:
    
    for i in reversed(range(n)):
       if not (n % i == 0):
            return i


