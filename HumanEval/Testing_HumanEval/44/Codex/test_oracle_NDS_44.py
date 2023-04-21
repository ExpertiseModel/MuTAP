def change_base(x: int, base: int):
    
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret





def test():
    assert change_base(11, 2) == "1011"
    assert change_base(15, 16) == "F"
    assert change_base(16, 16) == "10"
    assert change_base(17, 16) == "11"
    assert change_base(255, 16) == "FF"
    assert change_base(255, 2) == "11111111"
    
    
    
    
    
    assert change_base(0, 16) == "0"
    assert change_base(1, 16) == "1"
    assert change_base(10, 10) == "10"
    assert change_base(11, 10) == "11"
    assert change_base(12, 10) == "12"
    assert change_base(15, 10) == "15"
    assert change_base(16