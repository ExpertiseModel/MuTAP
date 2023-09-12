
def split_words(txt):
    
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',',' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])

# test case
def test():
    assert split_words("hello") == ["hello"]


    assert split_words("hello world") == ["hello\", \"world"]


    assert split_words(",hello,world,") == ["hello\", \"world"]


    assert split_words("hello,world,foo,bar") == ["hello\", \"world\", \"foo\", \"bar"]


    assert split_words("heLlO WoRlD") == ["hello\", \"world"]


    assert split_words("1hello23world") == ["1\", \"hello\", \"2\", \"world"] 