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


def test():
    assert words_string('a') == ['a']
    assert words_string('') == []
    assert words_string('a,b,c') == ['a','b','c']
