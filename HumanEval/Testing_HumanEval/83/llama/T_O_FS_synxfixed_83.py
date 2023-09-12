def starts_one_ends(n):
    
    if n == 1: 
        return 1
    return 18 * (10 ** (n - 2))


#</code>
#<test>
def test():
 
    assert starts_one_ends(1) == 1
    assert starts_one_ends(2) == 18
    assert starts_one_ends(3) == 540
    assert starts_one_ends(4) == 27772