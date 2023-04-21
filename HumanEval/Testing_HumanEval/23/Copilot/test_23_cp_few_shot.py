from script_23_cp_few_shot import strlen


def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('a') == 1
    assert strlen('ab') == 2
    assert strlen('abc') == 3
    assert strlen('abcd') == 4
    assert strlen('abcde') == 5
    assert strlen('abcdef') == 6
    assert strlen('abcdefg') == 7
    assert strlen('abcdefgh') == 8
    assert strlen('abcdefghi') == 9
    assert strlen('abcdefghij') == 10
    assert strlen('abcdefghijk') == 11


