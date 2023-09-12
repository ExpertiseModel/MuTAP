def is_palindrome(text: str):
    
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True




#</code>
#<test>
def test():
   

    # Test case 1: Valid palindrome
    assert is_palindrome("racecar") == True

    # Test case 2: Non-palindrome string
    assert is_palindrome("hello") == False

    # Test case 3: Palindrome with non-alphanumeric characters
    assert is_palindrome("level") == False

    # Test case 4: Palindrome with leading or trailing spaces
    assert is_palindrome("   racecar   ") == True

    ### Test case 5: Checking for palindrome with different lengths

    assert is_palindrome("level") == False