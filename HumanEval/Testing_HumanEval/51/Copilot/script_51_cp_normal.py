def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    """
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])


METADATA = {}


 # generate test case for the function above

def test_remove_vowels():
    assert remove_vowels("hello") == "hll"
    assert remove_vowels("world") == "wrld"
    assert remove_vowels("python") == "pythn"
    assert remove_vowels("javascript") == "jvscrpt"
    assert remove_vowels("java") == "jv"
    assert remove_vowels("ruby") == "rby"
    assert remove_vowels("php") == "ph"
    assert remove_vowels("c") == "c"
    assert remove_vowels("c++") == "c++"
    assert remove_vowels("c#") == "c#"
    assert remove_vowels("c") == "c"
    assert remove_vowels("c++") == "c++"
    assert remove_vowels("c#") == "c#"
    assert remove_vowels("c") == "c"
    assert remove_vowels("c++") == "c++"
    assert remove_vowels("c#") == "c#"
