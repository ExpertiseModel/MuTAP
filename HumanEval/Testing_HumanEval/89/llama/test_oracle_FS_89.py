def encrypt(s):
    
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 26]
        else:
            out += c
    return out


#</code>
#<test>
def test():

    assert encrypt("") == ""

    assert encrypt("a") == "a"

    assert encrypt("the quick brown fox jumps over the lazy dog") == "thedqbufoxjstlthedlf"

    encrypt("a") == "b"

    s = "ThE qUiCk BrOwN fOx jUmPs OvEr ThE LaZy DoG"
    assert encrypt(s