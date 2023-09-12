import script_13 as module_0


def test_case_0():
    int_0 = -44
    int_1 = module_0.greatest_common_divisor(int_0, int_0)
    assert int_1 == -44


def test_case_1():
    bool_0 = False
    int_0 = module_0.greatest_common_divisor(bool_0, bool_0)
    assert int_0 is False


def test_case_2():
    int_0 = 639
    int_1 = module_0.greatest_common_divisor(int_0, int_0)
    assert int_1 == 639
    int_2 = module_0.greatest_common_divisor(int_0, int_0)
    assert int_2 == 639
    int_3 = 2227
    none_type_0 = None
    int_4 = module_0.greatest_common_divisor(int_3, none_type_0)
    assert int_4 == 2227
    int_5 = 58
    int_6 = module_0.greatest_common_divisor(int_5, int_0)
    assert int_6 == 1
    int_7 = module_0.greatest_common_divisor(int_0, int_0)
    assert int_7 == 639
    int_8 = module_0.greatest_common_divisor(int_0, int_0)
    assert int_8 == 639
    int_9 = module_0.greatest_common_divisor(int_8, int_8)
    assert int_9 == 639
