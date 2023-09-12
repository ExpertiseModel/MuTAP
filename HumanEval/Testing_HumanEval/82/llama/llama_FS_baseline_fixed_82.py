def prime_length(string):
    
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True


#</code>
#<test>

def test():
    assert prime_length("4") == False
    assert prime_length("1") == False
    assert prime_length("1000") == False
