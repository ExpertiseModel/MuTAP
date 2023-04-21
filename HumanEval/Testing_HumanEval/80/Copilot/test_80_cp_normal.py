from script_80_cp_normal import is_happy

def test_is_happy():
    assert is_happy("abc") == True
    assert is_happy("abca") == False
    assert is_happy("abcab") == False
    assert is_happy("abcabc") == True
    assert is_happy("abcabcd") == False
    assert is_happy("abcabcde") == False
    assert is_happy("abcabcdef") == True
    assert is_happy("abcabcdefg") == False
    assert is_happy("abcabcdefgh") == False
    assert is_happy("abcabcdefghi") == True
    assert is_happy("abcabcdefghij") == False
    assert is_happy("abcabcdefghijk") == False
    assert is_happy("abcabcdefghijkl") == True
    assert is_happy("abcabcdefghijklm") == False
    assert is_happy("abcabcdefghijklmn") == False
    assert is_happy("abcabcdefghijklmno") == True
    