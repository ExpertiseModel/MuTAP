def sort_third(l: list):
    
    l = list(l)
    l[::3] = sorted(l[::3])
    return l




#</code>
#<test>
def test():
    
    assert sort_third([1, 2, 3]) == [1, 2, 3]

#</test case>

    assert sort_third([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    assert  sort_third([4, 2, 1, 3]) == [1, 2, 3, 4]



#</test case>

