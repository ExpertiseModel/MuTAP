def is_happy(s):
    
    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
        return False
    return True


# test case
def test():
    # Test with correct input
    assert is_happy("happy") == True
    assert is_happy("hello") == True
    # Test with incorrect input
    assert is_happy("haha") == False
    assert is_happy("") == False

# Test with different lengths
    assert is_happy("hello", 4) == False
    assert is_happy("hello", 5) == True

# Test with repeating characters

    assert is_happy("hello", 4, repeating=True) == False
    assert is_happy("hello", 4, repeating=True) == True

# Test with capital letters

    assert is_happy("HeLlO", 4) == False
    assert is_happy("HeLlO", 4) == True
