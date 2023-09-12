def change_base(x: int, base: int):
    
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret






#</code>
#<test>

def test():
    assert change_base(10, 2) == "1010"
    assert change_base(10, 3) == "101"
    assert change_base(10, 4) == "22"

    assert change_base(2, 10) == "2"
    assert change_base(2, 5) == "2"
    assert change_base(2, 2) == "10"

    assert change_base(3, 10) == "3"
    assert change_base(3, 2) == "11"
    assert change_base(3, 3) == "10"

    assert change_base(4, 10) == "4"
    assert change_base(3, 10) == "3"
    assert change_base(123, 3) == "11120"
    assert change_base(987, 2) == "1111011011"
    assert change_base(1000, 3) == "1101001"
    assert change_base(0, 10) == ""
