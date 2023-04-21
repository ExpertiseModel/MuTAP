from script_38_cp_few_shot import decode_cyclic


def test_decode_cyclic():
    assert decode_cyclic("abc") == "abc"
    assert decode_cyclic("a") == "a"
    assert decode_cyclic("ab") == "ab"
    assert decode_cyclic("abcde") == "bcaed"
    assert decode_cyclic("abcdefghi") == "bcaedfghi"
    assert decode_cyclic("abcdefghij") == "bcaedfghij"
    assert decode_cyclic("abcdefghijk") == "bcaedfghij"
    assert decode_cyclic("abcdefghijkl") == "bcaedfghij"
    assert decode_cyclic("abcdefghijklm") == "bcaedfghij"
    assert decode_cyclic("abcdefghijklmn") == "bcaedfghij"
    



