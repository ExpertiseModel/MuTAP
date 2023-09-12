def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

# test case

def test():
    assert digitSum("") ==  0
    assert digitSum("!@#$%") == 0
