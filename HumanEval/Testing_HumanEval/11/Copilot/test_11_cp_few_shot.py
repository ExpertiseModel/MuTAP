from script_11_cp_normal import string_xor


def test_string_xor() -> None:
    """ Test function for string_xor. """
    assert string_xor('0', '0') == '0'
    assert string_xor('0', '1') == '1'
    assert string_xor('1', '0') == '1'
    assert string_xor('1', '1') == '0'
    assert string_xor('000', '000') == '000'
    assert string_xor('000', '111') == '111'
    assert string_xor('111', '000') == '111'
    assert string_xor('111', '111') == '000'
    assert string_xor('11111111', '00000000') == '11111111'
    assert string_xor('11111111', '11111111') == '00000000'