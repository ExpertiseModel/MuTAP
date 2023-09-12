def skjkasdkd(lst):
    
    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False

        return True
    maxx = 0
    i = 0
    while i < len(lst):
        if(lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result



# test case
def test():
    
    # Test with a list of prime numbers
    # Verify the result
    assert skjkasdkd([2, 3, 5, 7, 11]) == 21

    # Test with a list of non-prime numbers

    # Verify the result
    assert skjkasdkd([4, 6, 8, 9, 10]) == 0

    # Test with a list of mixed prime and non-prime numbers

    # Verify the result
    assert skjkasdkd([2, 3, 5, 7, 11, 4, 6, 8, 9, 10]) == 21