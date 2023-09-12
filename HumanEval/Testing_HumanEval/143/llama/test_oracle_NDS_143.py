def words_in_sentence(sentence):
    
    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word)%i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)


# test case
def test():
    
    assert words_in_sentence("This is a simple sentence.") == "This is simple sentence."

    assert words_in_sentence("The quick brown fox jumps over the fence.") == "The quick brown fox jumps over the fence."

    assert words_in_sentence("The quick brown fox jumps over the fence quickly.") == "Quick brown fox jumps quickly over the fence."

    assert words_in_sentence("The quick brown fox jumped over the fence alone.") == "The quick brown fox alone jumped over the f