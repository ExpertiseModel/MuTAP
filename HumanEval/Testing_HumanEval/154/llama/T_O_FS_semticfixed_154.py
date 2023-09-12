def cycpattern_check(a , b):
    
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False


#</code>
#<test>

def test():
    assert cycpattern_check("", "") is True
    assert cycpattern_check("", "abc") is False

    assert cycpattern_check("abc", "") is True
    assert cycpattern_check("abc", "abc") is True

    assert cycpattern_check("abcdefg", "") is True
    assert cycpattern_check("abcdefg", "abcdefg") is True

    assert cycpattern_check("abc", "def") is False
    assert cycpattern_check("abc", "abcdefg") is False

    assert cycpattern_check("aababcdefg", "") is True
    assert cycpattern_check("aababcdefg", "aababcdefg") is True
