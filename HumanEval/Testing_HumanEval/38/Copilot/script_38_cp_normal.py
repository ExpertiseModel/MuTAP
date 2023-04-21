def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    return encode_cyclic(encode_cyclic(s))


METADATA = {}



 # generate test case for the function above

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
   