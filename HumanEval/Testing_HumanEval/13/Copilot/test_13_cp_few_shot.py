from script_13_cp_few_shot import greatest_common_divisor

def test_greatest_common_divisor():
    assert greatest_common_divisor(2, 4) == 2
    assert greatest_common_divisor(2, 3) == 1
    assert greatest_common_divisor(4, 6) == 2
    assert greatest_common_divisor(4, 9) == 1
    assert greatest_common_divisor(4, 8) == 4
    assert greatest_common_divisor(4, 0) == 4
    assert greatest_common_divisor(0, 0) == 0