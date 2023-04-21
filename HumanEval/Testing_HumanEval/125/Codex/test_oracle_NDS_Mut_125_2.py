def split_words(txt):
    
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',',' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])


def test():
    assert split_words(a) == ['a', 'b', 'c']
    assert split_words(a) == ['a', 'b', 'c']
    assert split_words(a) == ['a', 'b', 'c']
    assert split_words(a) == ['a', 'b', 'c']
    assert split_words(a) == ['a', 'b', 'c']
    try:
        assert split_words(a) == ['a', 'b', 'c']
    except:
        print('exception')
    assert split_words(a) == ['a', 'b', 'c']
    assert split_words(a) == ['a', 'b', 'c']
    assert split_words(a) == ['a', 'b', 'c']
    assert split_words(a) == ['a', 'b