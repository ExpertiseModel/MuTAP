def get_positive(l: list):
    
    return [e for e in l if e > 0]




#</code>
#<test>
def test():
    assert get_positive([1, 2, 3, 4, 5]) == [2, 3, 4, 5]


#<test case>

    assert get_positive([1, -2, -3, -4, -5]) == []


#<test case>
    assert get_positive([]) == []



#<test case>
    assert get_positive([1, 2, 3, -4, 5]) == [2, 3, 5]



#<test>











