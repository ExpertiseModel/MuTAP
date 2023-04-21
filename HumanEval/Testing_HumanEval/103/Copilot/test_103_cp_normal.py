from script_103_cp_few_shot import rounded_avg
def test_rounded_avg():
    assert rounded_avg(1, 10) == '0b1011'
    assert rounded_avg(1, 100) == '0b1100101'
    assert rounded_avg(1, 1000) == '0b1001001001'
    assert rounded_avg(1, 10000) == '0b1000100010001'
    assert rounded_avg(1, 100000) == '0b1000010000100001'
