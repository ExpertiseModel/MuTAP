def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret


METADATA = {}



 # generate test case for the function above

def test_change_base():
    assert change_base(10, 2) == "1010"
    assert change_base(10, 3) == "11"
    assert change_base(10, 4) == "22"
    assert change_base(10, 5) == "20"
    assert change_base(10, 6) == "14"
    assert change_base(10, 7) == "13"
    assert change_base(10, 8) == "12"
    assert change_base(10, 9) == "11"