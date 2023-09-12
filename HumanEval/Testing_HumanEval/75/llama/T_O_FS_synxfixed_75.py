def is_multiply_prime(a):
    
    def is_prime(n):
        for j in range(2,n):
            if n%j == 0:
                return False
        return True




    for i in range(2,101):
        if not is_prime(i): continue
        for j in range(2,101):
            if not is_prime(j): continue
            for k in range(2,101):
                if not is_prime(k): continue
                if i*j*k == a: return True
    return False


#</code>
#<test>
def test():
  
    assert is_multiply_prime(2) == True
    assert is_multiply_prime(3) == True
    assert is_multiply_prime(5) == True
    assert is_multiply_prime(7) == True
    assert is_multiply_prime(11) == True
    assert is_multiply_prime(13) == True
    assert is_multiply_prime(17) == True
    assert is_multiply_prime(19) == True

    assert is_multiply_prime(6) == False
    assert is_multiply_prime(8) == False
    assert is_multiply_prime(9) == False
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(14) == False
    assert is_multiply_prime(15) == False