from script_103_cp_few_shot import rounded_avg
def test_rounded_avg():
    assert rounded_avg(1, 5) == "0b11"
    assert rounded_avg(7, 5) == -1
    assert rounded_avg(1, 1) == "0b1"
    assert rounded_avg(1, 6) == "0b11"
    assert rounded_avg(1, 7) == "0b11"
    assert rounded_avg(1, 8) == "0b100"
    assert rounded_avg(1, 9) == "0b100"