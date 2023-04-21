from script_38_cp_normal import decode_cyclic

def test_decode_cyclic():
    assert decode_cyclic("abc") == "abc"
    assert decode_cyclic("bcd") == "abc"
    assert decode_cyclic("cde") == "abc"
    assert decode_cyclic("def") == "abc"
    assert decode_cyclic("efg") == "abc"
    assert decode_cyclic("fgh") == "abc"
    assert decode_cyclic("ghi") == "abc"
    assert decode_cyclic("hij") == "abc"
    assert decode_cyclic("ijk") == "abc"
    assert decode_cyclic("jkl") == "abc"
    assert decode_cyclic("klm") == "abc"
   