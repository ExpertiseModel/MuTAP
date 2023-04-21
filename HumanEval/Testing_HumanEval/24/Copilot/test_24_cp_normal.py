from script_24_cp_normal import largest_divisor


def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(16) == 8
    assert largest_divisor(17) == 1
    assert largest_divisor(18) == 9