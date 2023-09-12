
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
