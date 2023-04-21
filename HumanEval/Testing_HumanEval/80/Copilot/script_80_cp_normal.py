def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    """
    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
        return False
    return True

 # generate test case for the function above

def test_is_happy():
    assert is_happy("abc") == True
    assert is_happy("abca") == False
    assert is_happy("abcab") == False
    assert is_happy("abcabc") == True
    assert is_happy("abcabcd") == False
    assert is_happy("abcabcde") == False
    assert is_happy("abcabcdef") == True
    assert is_happy("abcabcdefg") == False
    assert is_happy("abcabcdefgh") == False
    assert is_happy("abcabcdefghi") == True
    assert is_happy("abcabcdefghij") == False
    assert is_happy("abcabcdefghijk") == False
    assert is_happy("abcabcdefghijkl") == True
    assert is_happy("abcabcdefghijklm") == False
    assert is_happy("abcabcdefghijklmn") == False
    assert is_happy("abcabcdefghijklmno") == True
    