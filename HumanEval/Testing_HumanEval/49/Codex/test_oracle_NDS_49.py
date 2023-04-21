def modp(n: int, p: int):
    
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret



def test():
    ...
    
    assert modp(2, 3) == 1
    assert modp(4, 3) == 3
    assert modp(5, 3) == 0
    assert modp(7, 3) == 1
    assert modp(10, 3) == 1

    assert modp(2, 7) == 4
    assert modp(4, 7) == 4
    assert modp(7, 7) == 3
    assert modp(10, 7) == 6

    assert modp(2, 11) == 3
    assert modp(4, 11) == 7
    assert modp(7, 11) == 8
    ...
