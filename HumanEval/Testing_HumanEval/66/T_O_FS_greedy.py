def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)assert digitSum('HE2llO0W0RlD') == 457
