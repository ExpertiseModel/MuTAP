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



def test():
    assert histogram("a a a a  b c d a a") == {'a': 4, 'b': 1, 'c': 1, 'd': 1}


`
