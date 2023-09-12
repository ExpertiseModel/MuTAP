def select_words(s, n):
    
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() not in ["a","e","i","o","u"]:
                n_consonants += 1 
        if n_consonants == n:
            result.append(word)
    return result



# test case

def test():
    # Test 1: Valid input

    assert select_words("Hello World!", 2) == []

    # Test 2: Valid input with multiple words
    assert select_words("The quick brown fox jumps over the lazy dog.", 3) == ['quick', 'lazy', 'dog.']

    # Test 3: Invalid input
    assert select_words("This is not a valid sentence.", 4) == []

    # Test 4: Valid input with too many consonants
    assert select_words("The quick brown fox jumps over the lazy dog.",5) == [ "brown"]
