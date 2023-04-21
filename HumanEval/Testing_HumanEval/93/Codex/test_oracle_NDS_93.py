def encode(message):
    
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])

def test():
    # ...
    assert encode("Hello") == "hELLO"
    assert encode("How are you?") == "HO wER re you?"
    assert encode("Is this your first time here?") == "is thi s your fIRST time here?"
    assert encode("This is a test.") == "This is a test."
    return "You passed all the tests!"

# test runner
if __name__ == '__main__':
    print test()
