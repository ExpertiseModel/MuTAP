def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans


METADATA = {}



 # generate test case for the function above

def test_fizz_buzz():
    assert fizz_buzz(0) == 0
    assert fizz_buzz(1) == 0
    assert fizz_buzz(10) == 0
    assert fizz_buzz(11) == 1
    assert fizz_buzz(12) == 1
    assert fizz_buzz(13) == 1
    assert fizz_buzz(14) == 1
    assert fizz_buzz(15) == 1
    assert fizz_buzz(16) == 1
    assert fizz_buzz(17) == 2
    assert fizz_buzz(18) == 2
    assert fizz_buzz(19) == 2
    