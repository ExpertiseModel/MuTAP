def is_happy(s):
    
    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
        return False
    return True


#</original code>


#<test>

def test():
    assert is_happy("hello") == False
    assert is_happy("aaabbb") == False
    assert is_happy("abbcccdd") == False
    assert is_happy("thequickbrownfoxjumpedoverthelazydog") == True
    assert is_happy("123456") == True
