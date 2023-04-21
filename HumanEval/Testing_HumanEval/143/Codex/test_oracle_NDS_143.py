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
    words_in_sentence('today is a good day')
    words_in_sentence('today is a bad day')
    words_in_sentence('today is a sunny day')
    words_in_sentence('today is a warm day')
    words_in_sentence('today is a cold day')
    words_in_sentence('today is a day today')
    words_in_sentence('today is a day day yesterday')

    # subtest
    assert words_in_sentence('today is a good day') == 'good'
    assert words_in_sentence('today is a bad day') == 'good'
    assert words_in_sentence('today is a sunny day') == 'sunny'
    assert words_in_sentence('today is a warm day') == 'warm'
    assert words_in_sent