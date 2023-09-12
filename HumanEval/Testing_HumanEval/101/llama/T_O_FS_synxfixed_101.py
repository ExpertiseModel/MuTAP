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
    assert words_string("apple") == ["a", "p", "p", "l", "e"]
    assert words_string("ABC") == ["A", "B", "C"]
    assert words_string("123, ABC") == ["1", "2", "3", "A", "B", "C"]
    assert words_string("a,b,c") == ["a", "b", "c"]
    assert words_string("This is a test") == ["T", "h", "i", "s", "a", "t", "e", "s", "t"]
#</test>
