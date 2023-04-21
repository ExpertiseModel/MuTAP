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
    assert solve("abc") == "ABC"
    assert solve("Abc") == "aBC"
    assert solve("") == ""
    assert solve("A") == "a"
    assert solve("a") == "A"
    assert solve("Et ai, ne") == "eT AI, NE"
    assert solve("abc") == "ABC"
    assert solve("Abc") == "aBC"
    assert solve("") == ""
    assert solve("A") == "a"
    assert solve("a") == "A"
    assert solve("Et ai, ne") == eT AI, NE
    assert solve("Et ai, ne") == eT AI, NE
    assert solve("abc") == "abc"
    assert solve("Et ai, ne") == eT AI, NE
