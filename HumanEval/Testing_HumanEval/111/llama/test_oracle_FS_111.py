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


#</code>
#<test>
def test():
    
    assert histogram("") == {}

    assert histogram("a") == {"a": 1}

    assert histogram("hello world") == {"h": 2, "e": 2, "l": 1, "o": 1, "w": 1}

def test_long_string():
    test_string = "this is a very long string with many characters"
    result = histogram("this is a very long string with many characters")
    assert histogram("this is a very long string with many characters") == {"t": 2, "h": 2, "i": 2, "s": 2, "a": 1, "v": 1, "e": 1, "r": 1}