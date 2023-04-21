def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)




def test():
    assert digitSum("abAB") == 131
    assert digitSum("abcCd") == 67
    assert digitSum("helloE") == 69
    assert digitSum("woArBld") == 131
    assert digitSum("aAaaaXa") == 153
    assert digitSum("abcCd") == 67
    assert digitSum("helloE") == 69
    assert digitSum("woArBld") == 131
    assert digitSum("aAaaaXa") == 153
    assert digitSum("") == 0
    assert digitSum("1234") == 0
    assert digitSum("Hello") == 72
    assert digitSum("!!") == 0
    assert digitSum("b") == 0
    assert digitSum("23456") == 0
    assert digitSum("$") == 0
    assert digitSum("aBcDeFg") == 204
