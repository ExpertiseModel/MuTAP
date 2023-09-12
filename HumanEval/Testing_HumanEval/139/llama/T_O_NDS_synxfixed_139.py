
def special_factorial(n):
 
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact


# test case
def test():
   
    # Test 1: Negative input
    assert special_factorial(-1) == 0

    # Test 2: Small input
    assert special_factorial(3) == 6

    # Test 3: Large input
    assert special_factorial(10) == 3628800

    # Test 4: Failure for non-positive input
    assert special_factorial(-2) == 0

    # Test 5: Non-integer input
  