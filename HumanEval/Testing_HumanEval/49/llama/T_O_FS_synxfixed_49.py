def modp(n: int, p: int):
    
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret




#</code>
#<test>
def test():
   
    assert modp(10, 7) == 3
    assert modp(10, 3) == 0
    assert modp(5, 7) == 2
    assert modp(10, 11) == 1
    assert modp(10, -3) == -2
    assert modp(5, -7) == -2
    assert modp(10, 0) == 0
    assert modp(5, 0) == 0
    assert modp(3, 2) == 0
    assert modp(3, 4) == 1
    assert modp(5, 3) == 0
    assert modp(4, 5) == 1
    assert modp(7, 3) == 0