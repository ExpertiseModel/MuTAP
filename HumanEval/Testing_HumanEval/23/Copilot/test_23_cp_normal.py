from script_23_cp_normal import strlen

def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('a') == 1
    assert strlen('ab') == 2