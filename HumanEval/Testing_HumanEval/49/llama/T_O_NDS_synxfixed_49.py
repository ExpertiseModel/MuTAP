def modp(n: int, p: int):
    
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret




# test case
def test():
    assert modp(10, 7) == 3
    assert modp(1000, 11) == 233
    assert modp(10, 3) == 1
    assert modp(10, 10000) ==  0