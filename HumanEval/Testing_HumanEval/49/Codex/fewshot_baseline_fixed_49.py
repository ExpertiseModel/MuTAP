def modp(n: int, p: int):
    
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret




def test():
    assert modp(6, 7) == 1
    assert modp(6, 11) == 9
