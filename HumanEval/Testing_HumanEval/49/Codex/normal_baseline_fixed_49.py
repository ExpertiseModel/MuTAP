def modp(n: int, p: int):
    
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret




def test():
    ...
    assert modp(5, 3) == 0
    assert modp(7, 3) == 1
