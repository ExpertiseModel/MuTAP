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


# test case

def test():
    # Test case 1: Valid string
    assert solve("hello") == "HELLO"
    # Test case 2: Uppercase to lowercase
    assert solve("HELLO") == "hello"
    # Test case 3: Lowercase to uppercase
    assert solve("hello") == "HELLO"
    # Test case 4: Number
    assert solve("1234") == "4321"
    # Test case 5: Special characters
    assert solve("#a@C") == "#A@c"
    # Test case 6: Empty string
    assert solve("") == ""

