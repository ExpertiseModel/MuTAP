def is_palindrome(text: str):
    
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True



def test():
    assert is_palindrome("abcd") == False
    assert is_palindrome("abcba") == True
    assert is_palindrome("abba") == True
    assert is_palindrome("") == True
    assert is_palindrome(" ") == False
    
    
if __name__ == "__main__":
    test()
