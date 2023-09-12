def largest_divisor(n: int) -> int:
    
    for i in reversed(range(n)):
        if n % i == 0:
            return i




# test case

def test():
