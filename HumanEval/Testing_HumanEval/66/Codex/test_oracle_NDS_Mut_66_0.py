def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)



def test():
    digitSum("abAB") == 131
    assert digitSum("abcCd") == 67
    assert digitSum("helloE") == 69
    assert digitSum("woArBld") == 131
    assert digitSum("aAaaaXa") == 153
    assert digitSum("") == 0
    assert digitSum("1234") == None
    assert digitSum("Hello") == None
    assert digitSum("!!") == None
    assert digitSum("b") == 1
    assert digitSum("23456") == 23
    assert digitSum("$") == None
    assert digitSum("aBcDeFg") == 68
    """
    digitSum("") => 0
    digitSum("abAB") => 131
    digitSum("abcCd") => 67
    digitSum("helloE") => 69
    digitSum("woArBld") => 131
