def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    """
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret


METADATA = {}



 # generate test case for the function above

def test_modp():
    assert modp(0, 2) == 1
    assert modp(1, 2) == 0
    assert modp(2, 2) == 0
    assert modp(3, 2) == 0
    assert modp(4, 2) == 0
    assert modp(5, 2) == 0
    assert modp(6, 2) == 0
    assert modp(7, 2) == 0
    assert modp(8, 2) == 0
    assert modp(9, 2) == 0
    assert modp(10, 2) == 0
    assert modp(11, 2) == 0
    assert modp(12, 2) == 0
    assert modp(13, 2) == 0
    assert modp(14, 2) == 0
    assert modp(15, 2) == 0
    assert modp(16, 2) == 0
    assert modp(17, 2) == 0
    assert modp(18, 2) == 0
    assert modp(19, 2) == 0
    assert modp(20, 2) == 0
   