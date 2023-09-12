def change_base(x: int, base: int):
    
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret






#</code>
#<test>
def test():
  
    assert change_base(10, 2) == "02"
    assert change_base(10, 3) == "03"
    assert change_base(10, 4) == "04"

    assert change_base(2, 10) == "0010"
    assert change_base(2, 5) == "0101"
    assert change_base(2, 2) == "0002"

    assert change_base(3, 10) == "0003"
    assert change_base(3, 2) == "0003"
    assert change_base(3, 3) == "0002"

    assert change_base(4, 10) == "000010"
    assert change_base(3, 10) == "0123456789"
    assert change_base(123, 3) == "456789"
    assert change_base(987, 2) == "196692"
    assert change_base(1000, 3) == "000000"
    assert change_base(0, 10) == ""