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
    assert encrypt('abcdefg') == 'defghij'
    assert encrypt('Hello World') == 'Upps Hjsvph'
    assert encrypt('Think Python') == 'Vlmro Jcxlsr'
    assert encrypt('1') == '1'
    assert encrypt('!') == '!'
    assert encrypt('') == ''
