def even_odd_count(num):
    
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)


#</code>
#<test>

def test():
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(3) == (0, 1)
    assert even_odd_count(4) == (1, 0)
    assert even_odd_count(-2) == (1, 0)
    assert even_odd_count(-3) == (0, 1)
    assert even_odd_count(5) == (0, 1)
    assert even_odd_count(6) == (1, 0)
    # Test corner cases
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(-1) == (0, 1)
    assert even_odd_count(7) == (0, 1)
    assert even_odd_count(8) == (1, 0)

