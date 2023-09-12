
def special_factorial(n):
    
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact


#</original code>



#<test>

def test():
    assert special_factorial(5) == 34560
    assert special_factorial(6) == 24883200
    assert special_factorial(7) == 125411328000
    assert special_factorial(8) == 5056584744960000
    assert special_factorial(9) == 1834933472251084800000
    assert special_factorial(10) == 6658606584104736522240000000
    assert special_factorial(11) == 265790267296391946810949632000000000
    assert special_factorial(12) == 127313963299399416749559771247411200000000000
