def special_factorial(n):
    
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact

def test():
    assert special_factorial(2) == 4
    assert special_factorial(3) == 10
    assert special_factorial(4) == 30
    assert special_factorial(5) == 120
    print("All tests passed!")


test()
