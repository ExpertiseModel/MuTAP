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
    select_words("asdfasdf", 1) == ["asdf"]
    assert select_words("aasdfasdfouoiu", 2) == ["aasdfasdfouoiu"]
    assert select_words("asdfasdf", 3) == ["asdf", "asdf", "asdf"]
    assert select_words("asdfasdf", 4) == []
