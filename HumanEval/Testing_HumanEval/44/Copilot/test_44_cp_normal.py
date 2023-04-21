from script_44_cp_normal import change_base

def test_change_base():
    assert change_base(10, 2) == "1010"
    assert change_base(10, 3) == "11"
    assert change_base(10, 4) == "22"
    assert change_base(10, 5) == "20"
    assert change_base(10, 6) == "14"
    assert change_base(10, 7) == "13"
    assert change_base(10, 8) == "12"
    assert change_base(10, 9) == "11"