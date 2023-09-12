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





def test():
    assert fizz_buzz(11) == 0
    assert fizz_buzz(22) == 0
    assert fizz_buzz(33) == 0
    assert fizz_buzz(44) == 0
    assert fizz_buzz(55) == 0
    assert fizz_buzz(66) == 0
    assert fizz_buzz(77) == 0
    assert fizz_buzz(88) == 3
    assert fizz_buzz(99) == 3
    assert fizz_buzz(0) == 0

    assert fizz_buzz(3) == 0
