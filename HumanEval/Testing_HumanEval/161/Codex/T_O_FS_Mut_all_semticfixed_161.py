def solve(s):
    
    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        if i.isalpha():
            new_str[idx] = i.swapcase()
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s




def test():
    assert solve("abcd") == "ABCD"
    assert solve("abcde") == "ABCDE"
    assert solve("aBcDe") == "AbCdE"
    assert solve("abcdE") == "ABCDe"
    assert solve("abbbcd") == "ABBBCD"
    assert solve("abbcdD") == "ABBCDd"
    assert solve("abcd") == "ABCD"
    assert solve("abcde") == "ABCDE"
    assert solve("aBcDe") == "AbCdE"
    assert solve("abcdE") == "ABCDe"
    assert solve("abbbcd") == "ABBBCD"
    assert solve("abbcdD") == "ABBCDd"
    assert solve(' ') ==  ' '
    assert solve('') == ''
    assert solve('hello') == 'HELLO'
    assert solve('HELLO') == 'hello'
    assert solve('hElLo') == 'HeLlO'
    assert solve('helloWorld') == 'HELLOwORLD'
    assert solve('HeLloWoRlD') == 'hElLOwOrLd'
    assert solve('HElLoWoRlD') == 'heLlOwOrLd'
    assert solve('HElLoWoRlD') == 'heLlOwOrLd'
    assert solve('HElLoWoRld') == 'heLlOwOrLD'
    assert solve('HeLlOwOrLd') == 'hElLoWoRlD'
    assert solve('helLoWorLd') == 'HELlOwORlD'
    assert solve('HElloWoRld') == 'heLLOwOrLD'
