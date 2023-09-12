def encode_shift(s: str):
    
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

# test case
def test():
  
    assert encode_shift("Hello World!") == "7eleHrLdWrld!"

    assert encode_shift("HeLlO WoRld!") == "7ehLloWrld!"

    assert decode_shift("7eleHrLdWrld!") == "Hello World!"

    assert decode_shift("7ehLloWrld!") == "HeLlO WoRld!"