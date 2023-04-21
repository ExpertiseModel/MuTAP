def change_base(x: int, base: int):
    
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret





def test():
    assert change_base(100, 2) == "1100100"
