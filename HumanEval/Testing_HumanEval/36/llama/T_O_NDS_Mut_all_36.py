
def fizz_buzz(n: int):
    
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans




# test case

def test():
    # Test case 1: Negative number of inputs
    assert fizz_buzz(-1) == 0

    # Test case 2: Negative number of inputs
    assert fizz_buzz(-2) == 0

    # Test case 1: Fizz input
    assert fizz_buzz(5) == 0
    assert fizz_buzz(12) == 12
    assert fizz_buzz(7) == 3
    # Test case 4: Mutation in the `for` loop
    # Expected output: 0
    assert fizz_buzz(0) == 0

    # Test case 5: Mutation in the `s` variable
    # Expected output: 0
    assert fizz_buzz(-1) == 0

    # Test case 6: Mutation in the `ans` variable
    # Expected output: 0
    assert fizz_buzz(1) == 1

    # Test case 7: Mutation in the `s` and `ans` variables
    # Expected output: 0
    assert fizz_buzz(2) == 0

    assert fizz_buzz(5) == 0
    assert fizz_buzz(10) == 5
