def next_smallest(lst):
    
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]


#</code>
#<test>
def test():
   
    assert next_smallest([]) is None

    assert next_smallest([1]) == [1]

    assert next_smallest([("banana", 1), ("orange", 2)]) == "orange"


    assert next_smallest([("banana", 1), ("orange", 2), ("apple", 3)]) == "apple"

    assert next_smallest([(1, "banana"), (2, "orange"), (3, "apple")]) == "apple"