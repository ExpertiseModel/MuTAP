def encode(message):
    
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])


# test case
def test():

    assert encode("") == ""


    assert encode("a") == "a"


    assert encode("aeiou") == "AEIOU"


    assert encode("bcdfghjklmnopqrstuvwxyz") == "BCDFGHJKLMNOPQRSTUVWXYZ"