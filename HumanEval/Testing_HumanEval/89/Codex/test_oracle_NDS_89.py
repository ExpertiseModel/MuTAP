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
    assert encrypt('aaaa') == 'cccc'
    assert encrypt('aAaAaA') == 'cCcCcC'
    assert encrypt('abcd') == 'efgh'
    assert encrypt('Abcd') == 'Efgh'
    assert encrypt('aaaaa') == 'ccccc'
    assert encrypt('AaaaAaAa') == 'CccCcCcC'
    assert encrypt('abcdefghijklmnopqrstuvwxyz') == 'efghijklmnopqrstuvwxyzabcdef'
    assert encrypt('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'efghijklmnopqrstuvwxyzabcdefABCDEFGHIJKLMNOPQRSTUVWXY'