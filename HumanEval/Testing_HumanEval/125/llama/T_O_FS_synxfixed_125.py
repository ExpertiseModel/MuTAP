def split_words(txt):
    
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',',' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])

#</code>
#<test>
def test():
    
    assert split_words("hello world") == ["hello", "world"]

    assert split_words("apple,banana") == ["apple", "banana"]

    assert split_words("ThisIsAnExample") == [ "This", "Is", "An", "Example" ]

    assert split_words("eight") == [8]

    assert split_words("") == []