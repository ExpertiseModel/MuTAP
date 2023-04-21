def even_odd_count(num):
    
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)


def test():
    assert even_odd_count(1345)== (1, 3)
    assert even_odd_count(-2747)== (2, 2)
    assert even_odd_count(-18)== (1, 1)
    assert even_odd_count(-23)== (1, 1)
