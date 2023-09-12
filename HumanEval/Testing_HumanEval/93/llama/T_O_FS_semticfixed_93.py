def encode(message):
    
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])


#</original code>


def test():
    assert encode("Hello World") == "hGLLQ wQRLD"
    assert encode("This is a test") == "tHKS KS C TGST"
    assert encode("Python is awesome") == "pYTHQN KS CWGSQMG"
    assert encode("ENCODING IS FUN!") == "gncqdkng ks fwn!"
    assert encode("This is a test message.") == "tHKS KS C TGST MGSSCGG."
