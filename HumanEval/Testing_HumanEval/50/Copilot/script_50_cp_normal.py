def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


METADATA = {}

# generate test case for the function above


def test_encode_shift():
    assert encode_shift("abc") == "fgh"
    assert encode_shift("def") == "ijk"
    assert encode_shift("ghi") == "lmn"
    assert encode_shift("jkl") == "opq"
    assert encode_shift("mno") == "rst"
    assert encode_shift("pqr") == "uvw"
    assert encode_shift("stu") == "xyz"
    assert encode_shift("wxy") == "bcd"
    assert encode_shift("xyz") == "cde"
    assert encode_shift("aaa") == "fff"
    assert encode_shift("zzz") == "eee"


def test_decode_shift():
    assert decode_shift("fgh") == "abc"
    assert decode_shift("ijk") == "def"
    assert decode_shift("lmn") == "ghi"
    assert decode_shift("opq") == "jkl"
    assert decode_shift("rst") == "mno"
    assert decode_shift("uvw") == "pqr"
    assert decode_shift("xyz") == "stu"
    assert decode_shift("bcd") == "wxy"
    assert decode_shift("cde") == "xyz"
    assert decode_shift("fff") == "aaa"
    assert decode_shift("eee") == "zzz"