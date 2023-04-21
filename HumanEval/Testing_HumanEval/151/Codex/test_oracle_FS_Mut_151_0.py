def double_the_difference(lst):
    
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])



def test():
    assert f(0) == 0
    assert f(13) == 28
    assert f(12) == 1
