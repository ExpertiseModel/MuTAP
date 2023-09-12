def count_upper(s):
    
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 1
    return count




#<test>

def test():
    assert count_upper("hello") == 0
    assert count_upper("hello world") == 0
    assert count_upper("uppercase") == 0
    assert count_upper("lowercase") == 0
    assert count_upper("digits") == 0
    assert count_upper("alphabet") == 0
