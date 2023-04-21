from script_78_cp_few_shot import hex_key


def test_hex_key():
    assert hex_key('') == 0
    assert hex_key('1') == 0
    assert hex_key('2') == 1
    assert hex_key('3') == 1
    assert hex_key('4') == 0
    assert hex_key('5') == 1
    assert hex_key('6') == 0
    assert hex_key('7') == 1
    assert hex_key('A') == 0
    assert hex_key('B') == 1
    assert hex_key('C') == 0
    assert hex_key('D') == 1
    assert hex_key('E') == 0
    assert hex_key('F') == 0
    assert hex_key('10') == 0
    assert hex_key('1A') == 0
    assert hex_key('1B') == 0
    assert hex_key('1C') == 0
    assert hex_key('1D') == 0
    assert hex_key('1E') == 0
    assert hex_key('1F') == 0
    assert hex_key('2A') == 0
    assert hex_key('2B') == 1



