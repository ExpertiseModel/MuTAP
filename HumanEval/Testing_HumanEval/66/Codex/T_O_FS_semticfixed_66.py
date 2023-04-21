def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

def test():
    assert digitSum('HE2llO0W0RlD') == 457
    assert digitSum('123') == 0
    assert digitSum('HELLO123') == 372
