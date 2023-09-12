def remove_vowels(text):
    
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])




#</code>
#<test>
def test():
   
    assert remove_vowels("Hello World!") == "Hl wrld!"
    assert remove_vowels("The quick brown fox jumps over the lazy dog.") == "Th quc brwn fx jmps vr thr lzy dg."
    assert remove_vowels("Python is a powerful programming language.") == "Pythn is a ppwrfl prgrmmng language."
    assert remove_vowels("The quick brown fox jumps over the lazy dog again.") == "Th quc brwn fx jmpsvr thr lzy dg agn."
    assert remove_vowels("Python is a powerful programming language that is easy to learn.") == "Pythn is a ppwrfl prgrmmng language tht  s easy to lrn."