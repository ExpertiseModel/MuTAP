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
    assert even_odd_count( 0) == (1, 0)
    assert even_odd_count( 1) == (0, 1)
    assert even_odd_count( 2) == (1, 0)
    assert even_odd_count( 3) == (0, 1)
    assert even_odd_count( -1) == (0, 1)
    assert even_odd_count( -2) == (1, 0)
    assert even_odd_count( -3) == (0, 1)
    assert even_odd_count( -11) == (0, 2)
    assert even_odd_count( 123) == (1, 2)
    assert even_odd_count( 234) == (2, 1)
    assert even_odd_count( -123) == (1, 2)
    assert even_odd_count
