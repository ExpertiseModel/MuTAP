def is_bored(S):
    
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)


# test case

def test():
    assert is_bored("I am bored.") ==  1

    assert is_bored("I am really bored.") == 1

    assert is_bored("I am so bored.") == 1

    assert is_bored("I am wondering if I am bored.") == 1

    assert is_bored("I am so bored!!") == 1
    assert is_bored("I (am bored.)") == 0

    assert is_bored("I (am really bored.)") == 0

    assert is_bored("I (am so bored.") == 0

    assert is_bored("I (am wondering if I am bored.") == 0

    assert is_bored("I (am so bored!!") == 0
    assert is_bored("") == 0
    assert is_bored("i AM Bored.") == 1
    assert is_bored("i Am Bored.") == 1
    assert is_bored("i Bored.") == 1
    assert is_bored("i BORED.") == 1
