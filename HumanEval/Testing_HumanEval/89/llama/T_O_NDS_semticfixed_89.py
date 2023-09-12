
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

