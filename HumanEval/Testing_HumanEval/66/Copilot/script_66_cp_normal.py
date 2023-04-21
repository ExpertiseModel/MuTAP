def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    """
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

 # generate test case for the function above

def test_digitSum():
    assert digitSum("") == 0
    assert digitSum("a") == 0
    assert digitSum("A") == 65
    assert digitSum("1") == 0
    assert digitSum("aA") == 65
    assert digitSum("a1") == 0
    assert digitSum("A1") == 65
    assert digitSum("aA1") == 65
    assert digitSum("aA1a") == 65
    assert digitSum("aA1A") == 130
    assert digitSum("aA1Aa") == 130