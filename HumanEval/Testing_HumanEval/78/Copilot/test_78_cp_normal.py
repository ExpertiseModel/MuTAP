from script_78_cp_normal import hex_key

def test_hex_key():
    assert hex_key('') == 0
    assert hex_key('1') == 0
    assert hex_key('2') == 1
    assert hex_key('3') == 1
    assert hex_key('4') == 0
    assert hex_key('5') == 1
    assert hex_key('6') == 0
    assert hex_key('7') == 1
    assert hex_key('8') == 0
    assert hex_key('9') == 0
    assert hex_key('A') == 0
    assert hex_key('B') == 1
    assert hex_key('C') == 0
    assert hex_key('D') == 1
    assert hex_key('E') == 0
    