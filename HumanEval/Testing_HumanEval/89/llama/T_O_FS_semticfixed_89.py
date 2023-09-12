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

    assert encrypt("a") == "e"

    assert encrypt("the quick brown fox jumps over the lazy dog") == "xli uymgo fvsar jsb nyqtw sziv xli pedc hsk"

    encrypt("a") == "b"

    s = "ThE qUiCk BrOwN fOx jUmPs OvEr ThE LaZy DoG"
