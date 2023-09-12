def histogram(test):
    
    dict1={}
    list1=test.split(" ")
    t=0

    for i in list1:
        if(list1.count(i)>t) and i!='':
            t=list1.count(i)
    if t>0:
        for i in list1:
            if(list1.count(i)==t):
                
                dict1[i]=t
    return dict1


# test case
def test():
   
    # Test 1: An empty string
    assert histogram(" ") == {}

    # Test 2: A single character string
    assert histogram("a") == {"a": 1}

    # Test 3: A multi-character string with no duplicates
    assert histogram("hello world") == {"h": 1, "l": 1, "o": 1, "w": 1}

    # Test 4: A multi-character string with duplicates
    assert histogram("hello world hello") == {"h": 2, "l": 2, "o": 2}

    # Test 5: An empty list
    assert histogram([]) == {}

    # Test 6: A list with repeats
    assert histogram(["a", "a", "b", "c", "a"]) == {"a": 2, "b": 1, "c": 1}
