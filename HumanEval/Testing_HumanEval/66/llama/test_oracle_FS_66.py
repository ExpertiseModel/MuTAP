def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

#</code>
#<test>
def test():
    
    # Test with a string of digits
    assert digitSum("123") == 6
    # Test with a string of letters
    assert digitSum("abc") == 0
    # Test with a string of mixed digits and letters
    assert digitSum("1a2b3c4") == 14
    # Test with an empty string
    assert digitSum("") == 0