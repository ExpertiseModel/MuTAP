def check_if_last_char_is_a_letter(txt):
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

def test():
    assert check_if_last_char_is_a_letter("This sentence has an apostrophe '") == True
    assert check_if_last_char_is_a_letter("This is a cool sentence.") == False
    assert check_if_last_char_is_a_letter("This one is even cooler.") == False
    assert check_if_last_char_is_a_letter("I also have a quote at the end of my string like \"This\"") == False
