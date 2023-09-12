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


#</code>
#<test>

def test():
    assert solve("1234567890") == "0987654321"


    assert solve("123456789A") == "123456789a"


    assert solve("123456789a") == "123456789A"

    assert solve("123456789a") == "123456789A"


