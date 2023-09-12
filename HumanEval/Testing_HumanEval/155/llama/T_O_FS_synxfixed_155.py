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
    
    assert even_odd_count(2) == (2, 0)
    assert even_odd_count(3) == (2, 1)
    assert even_odd_count(4) == (3, 1)
    assert even_odd_count(-2) == (1, 1)
    assert even_odd_count(-3) == (1, 2)
    assert even_odd_count(5) == (3, 2)
    assert even_odd_count(6) == (4, 2)
    # Test corner cases
    assert even_odd_count(0) == (0, 0)
    assert even_odd_count(-1) == (0, 1)
    assert even_odd_count(7) == (4, 2)
    assert even_odd_count(8) == (4, 3)
