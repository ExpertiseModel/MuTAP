def prime_length(string):
    
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

def test():
    prime_length("1") == False
    assert prime_length("") == False
    assert prime_length("111") == False
    assert prime_length("12") == False
    assert prime_length("1231") == False
    assert prime_length("1212") == False
    assert prime_length("12312") == False
    assert prime_length("1234321") == True
    assert prime_length("123432112344321") == True
    assert prime_length("123432112344321123454321") == True
    assert prime_length("12343211234432112345432112344321") == False
    assert prime_length("123454321123432112344321123454321") == False
    assert prime_length("") == False
    assert prime_length("1234543211234321123443