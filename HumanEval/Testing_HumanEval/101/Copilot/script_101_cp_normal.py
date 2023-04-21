def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    """
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

 # generate test case for the function above
def test_words_string():
    assert words_string("") == []
    assert words_string("Hello") == ["Hello"]
    assert words_string("Hello,") == ["Hello"]
    assert words_string("Hello, world!") == ["Hello", "world!"]
    assert words_string("Hello, world! ") == ["Hello", "world!"]
    assert words_string("Hello, world!  ") == ["Hello", "world!"]
    assert words_string("Hello, world!  ,") == ["Hello", "world!"]
    assert words_string("Hello, world!  , ") == ["Hello", "world!"]
    assert words_string("Hello, world!  , ,") == ["Hello", "world!"]
    assert words_string("Hello, world!  , , ") == ["Hello", "world!"]