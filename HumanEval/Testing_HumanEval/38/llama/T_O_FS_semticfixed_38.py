def encode_cyclic(s: str):
    
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    
    return encode_cyclic(encode_cyclic(s))




def test():
    assert encode_cyclic("") == ""

    assert encode_cyclic("a") == "a"

    assert encode_cyclic("abcdefg") == "bcaefdg"

    assert encode_cyclic("abcdefghijklmnop") == "bcaefdhigkljnomp"

    assert decode_cyclic("") == ""

# Test that encode_cyclic works correctly for single-character strings
    assert encode_cyclic("a") == "a"


# Test that encode_cyclic works correctly for strings with multiple characters
    assert encode_cyclic("hello") == "elhlo"


# Test that encode_cyclic works correctly for strings with punctuation
    assert encode_cyclic("!@#$%^&*()_+") == "@#!%^$*(&_+)"


# Test that encode_cyclic works correctly for strings with different lengths
    assert encode_cyclic("hello")[:3] == "elh"


# Test that decode_cyclic works correctly for encoded strings
    assert decode_cyclic("hdhll") == "hhdll"
