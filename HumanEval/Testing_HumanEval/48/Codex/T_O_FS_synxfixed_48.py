def is_palindrome(text: str):
    
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True



def test():
    assert is_palindrome("A car, a man, a maraca") == True
    assert is_palindrome("A car, a man, a maraca") == False
    assert is_palindrome("Madam I'm Adam") == True
    assert is_palindrome("A man, a plan, a canal - Panama") == True
    assert is_palindrome("A nut for a jar of tuna") == True
    assert is_palindrome("A Santa at Nasa") == True
