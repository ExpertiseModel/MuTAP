
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


# test case
def test():
    
    # Test with an empty string
    assert words_string("") == []
    # Test with a single letter
    assert words_string("a") == ["a"]
    # Test with a letter and a comma
    assert words_string("a,") == ["a", " "]
    # Test with multiple letters and commas
    assert words_string("a b c, d e") == ["a", "b", "c", " ", "d", "e"]
    # Test with a single letter and a space
    assert words_string("a ") == ["a", " ", ""]
    # Test with multiple letters and spaces
    assert words_string("a b c d e") == ["a", "b", "c", "d", "e"]
    # Test with a string that contains only letters and spaces
    assert words_string(" Hello, world!") == ["Hello", ",", "world"]
    # Test with a string that contains non-letters