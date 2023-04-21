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
    assert fix_spaces("This text") == "This_text"
    assert fix_spaces("This is muy     long text") == "This_is_muy_long____text"
    assert fix_spaces("This is a very long text") == "This_is_a_very_long_text"
    assert fix_spaces("This is a very düfūngly text") == "This_is_a_very_dufungly_text"
