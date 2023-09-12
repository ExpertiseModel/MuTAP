def total_match(lst1, lst2):
   
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2


#</code>
#<test>
def test():
  

    assert total_match(['apple', 'banana', 'cherry'], ['banana', 'cherry', 'date']) == ['apple', 'banana', 'cherry']

    assert total_match(['apple', 'banana', 'cherry'], ['banana', 'date', 'orange']) == ['banana', 'date', 'orange']
#

    assert total_match(['apple', 'banana', 'cherry'], ['banana', 'date', 'orange']) == ['banana']
#</testCase>

#<testCase>