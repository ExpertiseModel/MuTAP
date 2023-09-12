def next_smallest(lst):
    
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]


#</code>
#<test>

def test():
    assert next_smallest([]) is None
