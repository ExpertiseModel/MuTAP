def odd_count(lst):
    
    res = []
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
    return res
assert odd_count([[1,2,3,4,5,6,7]]) == ['the number of odd elements 4n the str4ng 4 of the 4nput.']
