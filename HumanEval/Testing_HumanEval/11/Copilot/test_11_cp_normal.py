from script_11_cp_normal import string_xor

def test_string_xor():
    assert string_xor('1010', '0101') == '1111'
    assert string_xor('1010', '1010') == '0000'
    assert string_xor('1010', '0111') == '1101'
    assert string_xor('1010', '1111') == '0101'
    assert string_xor('1010', '0000') == '1010'