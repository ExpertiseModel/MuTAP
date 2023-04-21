def is_happy(s):
    
    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
        return False
    return True



def test():

    assert is_happy('abc') == True
    assert is_happy('abcabc') == True
    assert is_happy('abcabcabc') == True
    assert is_happy('abcabcdef') == True
    assert is_happy('abcdefgabc') == True
    assert is_happy('adfdfdfdf') == False
    assert is_happy('happy') == False
    assert is_happy('false') == True
    assert is_happy('sing happy') == False
    assert is_happy('Unhappy') == False
    assert is_happy('12345678') == True
    assert is_happy('11110111') == False
    assert is_happy('01234567') == True
    assert is_happy('98765430') == True
    assert is_happy('987654300') == False
    assert is_happy('abc') == True
    assert is_happy('abcabc') == True
    assert is_happy('abcabcabc') == True
    assert is_happy('abcabcdef') == True
    assert is_happy('abcdefgabc') == True
    assert is_happy('adfdfdfdf') == False
    assert is_happy('happy') == False
    assert is_happy('false') == True
    assert is_happy('sing happy') == False
    assert is_happy('Unhappy') == False
    assert is_happy('12345678') == True
    assert is_happy('11110111') == False
    assert is_happy('01234567') == True
    assert is_happy('98765430') == True
    assert is_happy('987654300') == False

    assert is_happy([]) == False
    assert is_happy('abcabc') == True
    assert is_happy('abcabcabc') == True
    assert is_happy('abcabcdef') == True
    assert is_happy('abcdefgabc') == True
    assert is_happy('adfdfdfdf') == False
    assert is_happy('happy') == False
    assert is_happy('false') == True
    assert is_happy('sing') == False
    assert is_happy('Unhappy') == False
    assert is_happy('12345678') == True
    assert is_happy('11110111') == False
    assert is_happy('01234567') == True
    assert is_happy('98765430') == True
    assert is_happy('987654300') == False

