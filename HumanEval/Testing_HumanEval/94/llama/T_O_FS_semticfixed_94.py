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



#</code>
#<test>

def test():
    assert skjkasdkd([5, 3, 7, 11, 13]) == 4


    assert skjkasdkd([0, 1, 2, 3, 4]) == 3


    assert skjkasdkd([100, 1000, 10000, 100000, 1000000]) == 0


