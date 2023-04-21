from script_44_cp_few_shot import change_base


def test_change_base():
    assert change_base(0, 2) == "0"
    assert change_base(1, 2) == "1"
    assert change_base(2, 2) == "10"
    assert change_base(3, 2) == "11"
    assert change_base(4, 2) == "100"
    assert change_base(5, 2) == "101"
    assert change_base(6, 2) == "110"
    assert change_base(7, 2) == "111"
    assert change_base(8, 2) == "1000"
    assert change_base(9, 2) == "1001"



