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
    skjkasdkd([10,2,3,3]) == 0
    skjkasdkd([2, 3, 5, 3, 6, 7, 5, 6, 8]) == 7
    result = skjkasdkd([72,7,5,5,5,5,5,5,5,5,5,5,5,3,3,3,3,3,3])
    print(result)
    assert result == 70
    skjkasdkd([3,3,3,3]) == 0
    skjkasdkd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]) == 32
   