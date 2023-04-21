def remove_vowels(text):
    
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])




def test():
    assert remove_vowels("Milliways") == "Mllwys"
    assert remove_vowels("Theistareykjarbunga") == "Thstrykjrbng"
    assert remove_vowels("City of Gold and Diamonds") == "Cty f Gld nd Dmnds"
