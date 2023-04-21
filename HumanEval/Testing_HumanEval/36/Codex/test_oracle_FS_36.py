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
    fizz_buzz(0) == 0
    fizz_buzz(1) == 1
    fizz_buzz(2) == 2
    fizz_buzz(3) == 3
    fizz_buzz(4) == 4
    fizz_buzz(5) == 5
    fizz_buzz(6) == 6
    fizz_buzz(7) == 7
    fizz_buzz(8) == 8
    fizz_buzz(9) == 9
    fizz_buzz(10) == 10
    fizz_buzz(11) == 11
    fizz_buzz(12) == 12
    fizz_buzz(13) == 13
    fizz_buzz(14) == 14

    fizz_buzz(15) == 15
    fizz_buzz(