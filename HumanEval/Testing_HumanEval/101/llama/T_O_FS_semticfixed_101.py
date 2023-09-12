def words_string(s):
    
    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()



#<test>

def test():
    assert words_string("") == []
    assert words_string("apple") == ['apple']
    assert words_string("ABC") == ['ABC']
    assert words_string("123, ABC") == ['123', 'ABC']
    assert words_string("a,b,c") == ["a", "b", "c"]
    assert words_string("This is a test") == ['This', 'is', 'a', 'test']
#</test>

