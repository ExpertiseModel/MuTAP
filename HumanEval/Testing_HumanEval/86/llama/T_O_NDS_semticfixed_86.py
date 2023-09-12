
def anti_shuffle(s):
    
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])


# test case

def test():
    # Test with a small string
    assert anti_shuffle("Hello World") == "Hello Wdlor"
    # Test with a medium-sized string
    assert anti_shuffle("The quick brown fox jumps over the lazy dog") == "Teh cikqu bnorw fox jmpsu eorv eht alyz dgo"
    # Test with a long string
    assert anti_shuffle("The quick brown fox jumps over the lazy dog with excitement and joy") == "Teh cikqu bnorw fox jmpsu eorv eht alyz dgo hitw ceeeimnttx adn joy"
    # Test with multiple spaces in a word
    assert anti_shuffle("The quick brown fox jumps over the lazy dog with a big smile on his face") == "Teh cikqu bnorw fox jmpsu eorv eht alyz dgo hitw a bgi eilms no his acef"
    # Test with a string containing numbers
