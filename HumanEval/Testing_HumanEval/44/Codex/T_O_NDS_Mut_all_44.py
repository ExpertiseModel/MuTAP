def change_base(x: int, base: int):
    
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret







def test():

    assert change_base(11, 2) == "1011"
    assert change_base(15, 16) == "15"
    assert change_base(16, 16) == "10"
    assert change_base(17, 16) == "11"
    assert change_base(255, 16) == "1515"
    assert change_base(255, 2) == "11111111"
    assert change_base(255, 16) == "1515"
    
    
    
    
    assert change_base(0, 16) == "0"
