def encode(message):
    
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])


#</original code>

def test():
  
    assert encode("Hello World") == "Nle Wld"
    assert encode("This is a test") == "Tis is a tst"
    assert encode("Python is awesome") == "Pythn is Awesm"
    assert encode("ENCODING IS FUN!") == "ENCODINGISFUN!"
    assert encode("This is a test message.") == "THISISATESMT Msg"