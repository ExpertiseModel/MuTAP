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


def test():
    assert 
    assert 
    assert 
    assert 
    assert 

# automaticaly test when run 
# python -m  test_practice
if __name__ == "__main__":
    test()

