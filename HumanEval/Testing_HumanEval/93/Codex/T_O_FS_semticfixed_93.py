def encode(message):
    
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])


def test():
    assert encode("Hello") == hGLLQ
    assert encode("goodbye") == GQQDBYG
    assert encode("HELLO") == hgllq
    assert encode("GOODBYE") == gqqdbyg
    assert encode("MOM") == mqm
    assert encode("Dad") == dCD
    assert encode("JOEY") == jqgy
