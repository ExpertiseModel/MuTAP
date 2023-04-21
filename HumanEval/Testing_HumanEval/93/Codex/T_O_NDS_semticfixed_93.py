def encode(message):
    
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])


def test():
    assert encode("Hello") == hGLLQ
    assert encode("How are you?") == hQW CRG YQW?
    assert encode("Is this your first time here?") == kS THKS YQWR FKRST TKMG HGRG?
    assert encode("This is a test.") == tHKS KS C TGST.
