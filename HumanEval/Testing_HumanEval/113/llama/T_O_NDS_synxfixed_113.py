def odd_count(lst):
    
    res = []
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
    return res


# test case
def test():
 
    assert odd_count([]) == ["the number of odd elements 0n the str0ng 0 of the 0nput."]

    assert odd_count([1]) == ["the number of odd elements 1n the str1ng 1 of the 1nput."]

    assert odd_count([1, 2, 3, 4, 5]) == ["the number of odd elements 3n the str3ng 3 of the 3nput."]
    