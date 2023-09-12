from typing import List


def factorize(n: int) -> List[int]:
    
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return fact




#</original code>


#<test>

def test():
    assert factorize(3) == [3]
    assert factorize(4) == [2, 2]
