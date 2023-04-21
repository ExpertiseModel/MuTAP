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
    assert encrypt('aaaa') == 'eeee'
    assert encrypt('aAaAaA') == 'eAeAeA'
    assert encrypt('abcd') == 'efgh'
    assert encrypt('Abcd') == 'Afgh'
    assert encrypt('aaaaa') == 'eeeee'
    assert encrypt('AaaaAaAa') == 'AeeeAeAe'
    assert encrypt('abcdefghijklmnopqrstuvwxyz') == 'efghijklmnopqrstuvwxyzabcd'
    assert encrypt('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'efghijklmnopqrstuvwxyzabcdABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert encrypt('aaaa') == 'eeee'
    assert encrypt('aAaAaA') == 'eAeAeA'
    assert encrypt('abcd') == 'efgh'
    assert encrypt('Abcd') == 'Afgh'
    assert encrypt('aaaaa') == 'eeeee'
    assert encrypt('AaaaAaAa') == 'AeeeAeAe'
    assert encrypt('abcdefghijklmnopqrstuvwxyz') == 'efghijklmnopqrstuvwxyzabcd'
    assert encrypt('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'efghijklmnopqrstuvwxyzabcdABCDEFGHIJKLMNOPQRSTUVWXYZ'
