def encode_shift(s: str):
    
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

# test case

def test():
    assert encode_shift("Hello World!") == "gjqqtsvtwqit"

    assert encode_shift("HeLlO WoRld!") == "gjkqnsvtqqit"

    assert decode_shift("7eleHrLdWrld!") == "fzgzwmaylmgyj"

    assert decode_shift("7ehLloWrld!") == "fzcagjlmgyj"
