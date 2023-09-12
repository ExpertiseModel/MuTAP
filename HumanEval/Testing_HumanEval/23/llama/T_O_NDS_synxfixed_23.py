def strlen(string: str) -> int:
    
    return len(string)




# test case
def test():
    #test_empty_string
    assert strlen("") == 0

    #test_short_string
    assert strlen("hello") == 5

    #test_long_string
    assert strlen("a") == 1

    #test_string_with_spaces
    assert strlen("   hello   ") == 7

    #test_string_with_non_ascii_characters
    assert strlen("ñ") == 2

    #test_string_with_unicode_characters
    assert strlen("😊") == 5

    #test_edge_cases
    # assert strlen(b"") == 0

    #test_negative_number
    assert strlen(-1) == 0

    #test_non_string_object
    assert strlen({}) == 0