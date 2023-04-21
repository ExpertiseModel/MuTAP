def cycpattern_check(a , b):
    
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False




def test():
    assert cycpattern_check("AACCEE", "AACC") == True
    assert cycpattern_check("AACCEE", "C") == True
    assert cycpattern_check("ABCB", "ABC") == True
    assert cycpattern_check("AACCEE", "AACC") == True
    assert cycpattern_check("AACCEE", "AACC") == True
    assert cycpattern_check("", "AACCEE") == False
    assert cycpattern_check("AACCEE", "") == True
    assert cycpattern_check("AACCEE", None) == False    
    assert cycpattern_check("AACCEE", "AACC") == True
    assert cycpattern_check("AACCEE", "C") == True
    assert cycpattern_check("ABCB", "ABC") == True
    assert cycpattern_check("AACCEE", "AACC") == True
    assert cycpattern_check("AACCEE", "AACC") == True
    assert cycpattern_check("AACCEE", "AACC") == True
    assert cycpattern_check("AACCEE", "C") == True
    assert cycpattern_check("ABCB", "ABC") == True
    assert cycpattern_check("AACCEE", "AACC") == True
    assert cycpattern_check("AACCEE", "AACC") == True
    assert cycpattern_check("AACCEE", "C") == True
    assert cycpattern_check("ABCB", "ABC") == True
    assert cycpattern_check("AACCEE", "AACC") == True
    assert cycpattern_check("AACCEE", "AACC") == True
