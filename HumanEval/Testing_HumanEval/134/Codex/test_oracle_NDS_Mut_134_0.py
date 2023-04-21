def check_if_last_char_is_a_letter(txt):
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False



def test():
    assert check_if_last_char_is_a_letter("My last character is a letter") == False
    assert check_if_last_char_is_a_letter("Last Character") == False
    pytest.raises(Exception, check_if_last_char_is_a_letter, "!/#@$%")
    assert check_if_last_char_is_a_letter("1a") == False
    assert check_if_last_char_is_a_letter("a6") == False
