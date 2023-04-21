def fix_spaces(text):
   
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        if text[i] == " ":
            end += 1
        else:
            if end - start > 2:
                new_text += "-"+text[i]
            elif end - start > 0:
                new_text += "_"*(end - start)+text[i]
            else:
                new_text += text[i]
            start, end = i+1, i+1
        i+=1
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "_"
    return new_text



def test():
    assert fix_spaces("She had a cat.  She was a cat.  She was a cat.") == "She_had_a_cat.__She_was_a_cat.__She_was_a_cat."
    assert fix_spaces("It's it's a test") == "It's_it's_a_test"
    assert fix_spaces("It_s it's a test") == "It_s_it's_a_test"
    assert fix_spaces("It_s it's a test") == "It_s_it's_a_test"
    assert fix_spaces("It_s it's a test") == "It_s_it's_a_test"
    assert fix_spaces("It_s it's a test") == "It_s_it's_a_test"
