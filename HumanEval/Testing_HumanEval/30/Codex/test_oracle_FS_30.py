def get_positive(l: list):
    
    return [e for e in l if e > 0]



def test():
    assert get_positive([4, -9, 0, 5, 10]) == [4, 5, 10]
    assert 
