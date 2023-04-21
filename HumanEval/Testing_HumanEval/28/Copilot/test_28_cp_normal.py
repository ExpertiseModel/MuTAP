from script_28_cp_normal import concatenate

def test_concatenate():
    assert concatenate(["a", "b", "c"]) == "abc"
    assert concatenate(["a", "b", "c", "d"]) == "abcd"
    assert concatenate(["a", "b", "c", "d", "e"]) == "abcde"
    assert concatenate(["a", "b", "c", "d", "e", "f"]) == "abcdef"
    assert concatenate(["a", "b", "c", "d", "e", "f", "g"]) == "abcdefg"
    assert concatenate(["a", "b", "c", "d", "e", "f", "g", "h"]) == "abcdefgh"
    assert concatenate(["a", "b", "c", "d", "e", "f", "g", "h", "i"]) == "abcdefghi"
    assert concatenate(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]) == "abcdefghij"
    assert concatenate(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]) == "abcdefghijk"
 