def odd_count(lst):
    
    res = []
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
    return res


#</code>
#<test>
def test():
 
    assert odd_count([]) == ["The number of odd elements 0 in the list."]


    assert odd_count([1]) == ["The number of odd elements 1 in the list."]

    assert odd_count([1, 3, 5, 7, 9]) == ["The number of odd elements 3 in the list.", "The number of odd elements 5 in the list.", "The number of odd elements 7 in the list.", "The number of odd elements 9 in the list."]

    assert odd_count([2, 4, 6, 8, 10]) == ["The number of odd elements 0 in the list.", "The number of odd elements 2 in