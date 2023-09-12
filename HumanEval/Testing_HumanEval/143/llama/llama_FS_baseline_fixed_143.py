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


#</code>
#<test>

def test():
    assert words_in_sentence("") == ""
    assert words_in_sentence("hello") == "hello"
    assert words_in_sentence("big") == "big"
