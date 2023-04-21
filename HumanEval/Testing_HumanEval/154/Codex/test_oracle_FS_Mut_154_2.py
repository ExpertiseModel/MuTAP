def cycpattern_check(a , b):
    
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False



def test():
    #too long input
    assert cycpattern_check("", "AACCEE") == False
    #target shorter than pattern
    assert cycpattern_check("AACCEE", "") == False
    #pattern is None 
    assert cycpattern_check("AACCEE", None) == False
test()
