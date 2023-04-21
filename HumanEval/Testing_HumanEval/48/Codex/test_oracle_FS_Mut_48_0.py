def is_palindrome(text: str):
    
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True





def test():
    assert assertion_funcion_name == 'is_palindrome'
    assert True == expected result
    assert 'To be a palindrome, a string should' == assertion message, 'One or more of the assertions failed!'
