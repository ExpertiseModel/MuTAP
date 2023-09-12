def remove_vowels(text):
    
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])




# test case

def test():
    assert remove_vowels("") == ""

    assert remove_vowels("a") == ""

    assert remove_vowels("ae") == ""

    assert remove_vowels("aie") == ""

    assert remove_vowels("aio") == ""

    assert remove_vowels("aieu") == ""
