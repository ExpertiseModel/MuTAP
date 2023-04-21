def encode_shift(s: str):
    
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
def test():
    encode_shift("abc") == encode_shift("ABC") == "def"
    assert decode_shift("def") == decode_shift("DEF") == "ABC"
    assert encode_shift("abc") == decode_shift(encode_shift("abc")) == "abc"
    assert encode_shift("abcabcabcabc") == decode_shift(decode_shift("abcabcabcabc")) == "abcabcabcabc"
