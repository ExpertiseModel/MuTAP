def count_upper(s):
    
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 1
    return count

def test():
    assert count_upper('WHO ARE YOU?') == 0
    assert count_upper('I AM') == 1
    assert count_upper('I AM A NamE') == 1
    assert count_upper('I am') == 0
    assert count_upper('I am a person') == 0
    assert count_upper('I am a Name') == 1
    print('All test cases passed!')

test()

