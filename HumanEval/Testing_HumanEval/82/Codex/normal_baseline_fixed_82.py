def prime_length(string):
    
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True


def test():
    assert prime_length('2') == False
    assert prime_length('6') == False
    assert prime_length('101') == True
    assert prime_length('1100') == False
