def is_palindrome(text: str):
    
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True




# test case
def test():
# Test 1: Valid palindrome
#test_valid_palindrome():
    assert is_palindrome("racecar") == True

    # Test 2: Invalid palindrome
    #test_invalid_palindrome():
    assert is_palindrome("hello") == False

    # Test 3: Edge cases
    #test_edge_cases():
    assert is_palindrome("") == False

    # Test 4: Reverse case
    #test_reverse_case():
    assert is_palindrome("racecar") == True

    # Test 5: Multiple words
    #test_multiple_words():
    assert is_palindrome("foobar") == False