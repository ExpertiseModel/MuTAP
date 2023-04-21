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
    assert words_string("") == []
    assert words_string("Hello") == ['H', 'e', 'l', 'l', 'o']
    assert words_string("Hello, World!") == ['H', 'e', 'l', 'l', 'o', '', 'W', 'o', 'r', 'l', 'd', '!']
    assert words_string("Hello, World, my name is kim") == ['H', 'e', 'l', 'l', 'o', '', 'W', 'o', 'r', 'l', 'd', '', 'm', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'k', 'i', 'm']
