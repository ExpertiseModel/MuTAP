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
    assert encrypt('abcdefg') == 'fedcba'
    assert encrypt('Hello World') == 'Jgnnq Curc'
    assert encrypt('Think Python') == 'Wkhn phxzq'
    