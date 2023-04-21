from script_13_cp_few_shot import greatest_common_divisor

def test_greatest_common_divisor():
    assert greatest_common_divisor(1, 1) == 1
    assert greatest_common_divisor(1, 2) == 1
    assert greatest_common_divisor(2, 1) == 1
    assert greatest_common_divisor(2, 2) == 2
    assert greatest_common_divisor(2, 3) == 1
    assert greatest_common_divisor(3, 2) == 1
    assert greatest_common_divisor(3, 3) == 3
    assert greatest_common_divisor(3, 4) == 1
    assert greatest_common_divisor(4, 3) == 1
    assert greatest_common_divisor(4, 4) == 4
    assert greatest_common_divisor(4, 5) == 1
    assert greatest_common_divisor(5, 4) == 1
    assert greatest_common_divisor(5, 5) == 5
    assert greatest_common_divisor(5, 6) == 1
    assert greatest_common_divisor(6, 5) == 1
    assert greatest_common_divisor(6, 6) == 6
    assert greatest_common_divisor(6, 7) == 1
    assert greatest_common_divisor(7, 6) == 1
    assert greatest_common_divisor(7, 7) == 7