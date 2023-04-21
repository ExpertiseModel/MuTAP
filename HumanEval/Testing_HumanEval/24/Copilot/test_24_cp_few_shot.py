from script_24_cp_few_shot import largest_divisor


def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(16) == 8
    assert largest_divisor(17) == 1
    assert largest_divisor(18) == 9
    assert largest_divisor(19) == 1
    assert largest_divisor(20) == 10
    assert largest_divisor(21) == 7


