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
`skjkasdkd([10,2,3,3])` is an array with 0, 2, 3, 3.

The next step is to let `assert` check the change in
`skjkasdkd(lst)`.

