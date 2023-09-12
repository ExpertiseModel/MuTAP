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



#</code>
#<test>

def test():
    assert select_words("", 2) == []


    assert select_words("a", 1) == []


    assert select_words("hello", 3) == ['hello']


    assert select_words("banana", 3) == ['banana']
