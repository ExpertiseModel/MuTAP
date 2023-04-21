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




def test():

    skjkasdkd([10,2,3,3]) == 0    assert skjkasdkd([10,2,3,3]) == 0

    assert skjkasdkd([10,2,3,3]) == 0
    assert skjkasdkd([10,12,3,3]) == 3
    assert skjkasdkd([10,12,15,3]) == 15

    assert res == excepted_res

    assert skjkasdkd([10,2,3,3]) == 0
    assert skjkasdkd([10,2,3,4]) == 0
    assert skjkasdkd([10,2,3,5]) == 0

    assert skjkasdkd([410000, 420000, 430000, 440000, 450000, 460000, 470000]) == 0

