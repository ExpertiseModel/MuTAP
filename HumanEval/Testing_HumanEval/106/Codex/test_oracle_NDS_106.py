def f(n):
    
    ret = []
    for i in range(1,n+1):
        if i%2 == 0:
            x = 1
            for j in range(1,i+1): x *= j
            ret += [x]
        else:
            x = 0
            for j in range(1,i+1): x += j
            ret += [x]
    return ret

def test():
#test()
assert 2 == f(2)
assert [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] == f(10)
assert [1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] == f(11)
assert [1, 0, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144] == f(12)

# run
f(10)

# run : 
# ls -lh .
# wc -l ./*.py
# wc -l ./*.py|sort -g -k1
