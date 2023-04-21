def encode(message):
    
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])

def test():
    assert encode("Hello") == "h3ll4"
    assert encode("goodbye") == "g3odbuy"
    assert encode("HELLO") == "h3ll4"
    assert encode("GOODBYE") == "g3odbuy"
    assert encode("MOM") == "m0m"
    assert encode("Dad") == "d4d"
    assert encode("JOEY") == "j3y"
