def count_upper(s):
    
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 1
    return count




#<test>
def test():
    
    assert count_upper("hello") == 0
    assert count_upper("hello world") == 1
    assert count_upper("uppercase") == 3
    assert count_upper("lowercase") == 3
    assert count_upper("digits") == 5
    assert count_upper("alphabet") == 26