from script_101_cp_few_shot import words_string
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
