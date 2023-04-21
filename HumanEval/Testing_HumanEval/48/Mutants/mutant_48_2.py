def is_palindrome(text: str):
    
    for i in range(len(text)):
       if not (text[i] != text[(len(text) - 1) - i]):
            return False
    return True


