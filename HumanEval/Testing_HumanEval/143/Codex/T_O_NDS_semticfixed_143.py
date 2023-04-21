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


def test():
    assert words_in_sentence('today is a good day') == 'today is day'
    assert words_in_sentence('today is a bad day') == 'today is bad day'
    assert words_in_sentence('today is a sunny day') == 'today is sunny day'
    assert words_in_sentence('today is a warm day') == 'today is day'
