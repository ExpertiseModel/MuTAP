def remove_vowels(text):
    
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])




#</code>
#<test>

def test():
    assert remove_vowels("Hello World!") == "Hll Wrld!"
    assert remove_vowels("The quick brown fox jumps over the lazy dog.") == "Th qck brwn fx jmps vr th lzy dg."
    assert remove_vowels("Python is a powerful programming language.") == "Pythn s  pwrfl prgrmmng lngg."
    assert remove_vowels("The quick brown fox jumps over the lazy dog again.") == "Th qck brwn fx jmps vr th lzy dg gn."
    assert remove_vowels("Python is a powerful programming language that is easy to learn.") == "Pythn s  pwrfl prgrmmng lngg tht s sy t lrn."
