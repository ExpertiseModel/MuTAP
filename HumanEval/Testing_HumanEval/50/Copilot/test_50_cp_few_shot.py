from script_50_cp_few_shot import encode_shift


def test_encode_shift():
    assert encode_shift("a") == "f"
    assert encode_shift("b") == "g"
    assert encode_shift("c") == "h"
    assert encode_shift("d") == "i"
    assert encode_shift("e") == "j"
    assert encode_shift("z") == "e"
    assert encode_shift("y") == "d"
    assert encode_shift("x") == "c"
    assert encode_shift("w") == "b"
    assert encode_shift("v") == "a"
    assert encode_shift("") == ""
    assert encode_shift(" ") == " "
    assert encode_shift("abcde") == "fghij"
    assert encode_shift("xyz") == "cde"
    assert encode_shift("wxyz") == "bcde"
    assert encode_shift("vwxyz") == "abcde"
    assert encode_shift("vwxyz ") == "abcde "
    assert encode_shift("vwxyz ") == "abcde "





