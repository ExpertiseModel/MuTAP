def encode_shift(s: str):
    
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
def test():

def test():
    assert decode_shift("bcd") == "abc"
    assert decode_shift("bcd") == "abc"
    assert decode_shift("hij") == "hgi"
    assert decode_shift("hij") == "hgi"
    assert decode_shift("klm") == "kln"
    assert decode_shift("klm") == "kln"
    assert decode_shift("pqr") == "pqs"
    assert decode_shift("pqr") == "pqs"
    assert decode_shift("stu") == "stv"
    assert decode_shift("stu") == "stv"
