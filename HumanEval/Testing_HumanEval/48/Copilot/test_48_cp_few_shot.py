from script_48_cp_few_shot import is_palindrome


def test_is_palindrome():
    assert is_palindrome("") == True
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



