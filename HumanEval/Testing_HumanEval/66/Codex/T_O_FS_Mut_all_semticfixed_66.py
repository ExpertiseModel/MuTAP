def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)



def test():
    assert digitSum('HE2llO0W0RlD') == 457
    assert digitSum('123') == 0
    assert digitSum('HELLO123') == 372
    assert digitSum('123') == 0
    assert digitSum('') == 0
    assert digitSum('abAB') == 131
    assert digitSum('abcCd') == 67
    assert digitSum('helloE') == 69
    assert digitSum("!!") == 0
    assert digitSum('woArBld') == 131
    assert digitSum('aAaaaXa') == 153
