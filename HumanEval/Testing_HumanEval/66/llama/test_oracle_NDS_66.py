def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

# test case
def test():
    assert digitSum("") ==  0
    
    assert digitSum("hello") ==  7
    
    assert digitSum("HELLO")==  7
    
    assert digitSum("HeLlO") ==  7
    
    assert digitSum("   Hello   ") == 7

    assert digitSum("!@#$%") == 0