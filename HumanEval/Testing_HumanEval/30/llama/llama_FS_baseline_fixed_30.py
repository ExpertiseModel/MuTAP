def get_positive(l: list):
    
    return [e for e in l if e > 0]




#</code>
#<test>

def test():
    assert get_positive([]) == []
