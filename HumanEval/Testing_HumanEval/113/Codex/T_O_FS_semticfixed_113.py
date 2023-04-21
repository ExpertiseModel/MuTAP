def odd_count(lst):
    
    res = []
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
    return res


def test():
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0, 0.0], 0.95) == False    
    assert has_close_elements([1.0, 3.0, 5.9, 4.0, 5.0, 0.0], 0.95) == True    
    assert has_close_elements([0.0, 0.0, 0.0], 0.95) == False    
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True    
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.05) == False