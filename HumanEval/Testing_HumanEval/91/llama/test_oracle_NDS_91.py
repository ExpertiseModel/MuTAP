def is_bored(S):
    
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)


# test case
def test():

    assert is_bored("I am bored.") ==  1

    assert is_bored("I am really bored.") == 2

    assert is_bored("I am so bored.") == 1

    assert is_bored("I am wondering if I am bored.") == 1

    assert is_bored("I am so bored!!") == 1