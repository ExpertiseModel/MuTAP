def change_base(x: int, base: int):
    
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret






#</code>
#<test>

def test():
    assert change_base(0, 10) == ""
