def encrypt(s):
    
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 26]
        else:
            out += c
    return out


def test():
    assert encrypt('abcdefg') == 'efghijk'
    assert encrypt('Hello World') == 'Hipps Wsvph'
    assert encrypt('Think Python') == 'Tlmro Pcxlsr'
   