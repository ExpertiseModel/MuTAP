
def encrypt(s):
    
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 26]
        else:
            out += c
    return out


# test case

def test():
    assert encrypt("") == ""


    assert encrypt("a") == "e"


    assert encrypt("AbaCaDoEfGhIjKlMnOqRtUvWxyZ") == "AfeCeDsEjGlInKpMrOuRxUzWbcZ"


    assert encrypt("1234567890") == "1234567890"
    assert encrypt("AbaCaDoEfGhIjKlMnOqRtUvWxyZ") == "AfeCeDsEjGlInKpMrOuRxUzWbcZ"
    # Try a different input, but with a subtle change
    assert encrypt("1234567890") == "1234567890"
    # Try inputting a character that doesn't exist in the substitution cipher
    assert encrypt("XyzAbcDeFgHiJkLmNopQrStUvWxyZ") == "XyzAbcDeFgHiJkLmNopQrStUvWbcZ"

