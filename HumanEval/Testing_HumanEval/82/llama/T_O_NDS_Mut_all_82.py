def prime_length(string):
    
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True


# test case

def test():
    assert prime_length("5") == False

    assert prime_length("ABC") == True
    
    assert prime_length("5") == False
    assert prime_length("10") == True
    assert prime_length("20") == True
    assert prime_length("30") == True
    assert prime_length("20") == True
    assert prime_length("40") == True
    assert prime_length("60") == True
    assert prime_length("80") == True
    #mutant input
    assert prime_length("2*20") == False
    assert prime_length("4*20") == False
    assert prime_length("6*20") == False
    assert prime_length("8*20") == False
   
