def encode_shift(s: str):
    
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

#</code>
#<test>
def test():
   
    assert encode_shift("hello") == "4h5e7l7o"
    assert decode_shift("4h5e7l7o") == "hello"
    assert encode_shift(" ABC") == "3a4b7c"
    assert decode_shift("3a4b7c") == " ABC"
    assert encode_shift("123") == "31243"
    assert decode_shift("31243") == "123"
    # Test edge cases
    assert encode_shift("") == ""
    assert encode_shift(None) == ""
    assert decode_shift("") == ""
    assert decode_shift(None) == ""
    # Test different types of inputs
    assert encode_shift(42) == "425e7l7o"
    assert decode_shift("425e7l7o") == "42"