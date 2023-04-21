def is_palindrome(text: str):
    
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True





def test():
    assert is_palindrome("A car, a man, a maraca") == False
    assert is_palindrome("A car, a man, a maraca") == False
    assert is_palindrome("Madam I'm Adam") == False
    assert is_palindrome("A man, a plan, a canal - Panama") == False
    assert is_palindrome("A nut for a jar of tuna") == False
    assert is_palindrome("A Santa at Nasa") == False
    assert is_palindrome('A car, a man, a maraca') == False
    assert is_palindrome('A car, a man, a maraca') == False
    assert is_palindrome('Madam I\'m Adam') == False
    assert is_palindrome('A man, a plan, a canal - Panama') == False
    assert is_palindrome('A nut for a jar of tuna') == False
    assert is_palindrome('A Santa at Nasa') == False
    assert is_palindrome(" ") == True
    assert is_palindrome("a") == True
    assert is_palindrome("") == True


