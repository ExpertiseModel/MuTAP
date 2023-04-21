def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    """
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True


METADATA = {}



 # generate test case for the function above

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("bob") == True
    assert is_palindrome("mom") == True
    assert is_palindrome("dad") == True
    assert is_palindrome("level") == True
    assert is_palindrome("noon") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("refer") == True
    assert is_palindrome("deified") == True
    assert is_palindrome("civic") == True
    assert is_palindrome("rotator") == True
    assert is_palindrome("kayak") == True
    assert is_palindrome("reviver") == True