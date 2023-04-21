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
    assert histogram("an ant str") == {'an': 1, 'ant': 1, 'str': 1}
    assert histogram("an ant ant") == {'an': 2, 'ant': 2}
    assert histogram("") == {'': 1}
    assert histogram("a") == {'a': 1}
    assert histogram("a a") == {'a': 2}
    assert histogram("tricky") == {"t": 1, "r": 1, "i": 1, "c": 1, "k": 1, "y": 1}
    assert histogram("e e e e") == {"e": 4}
    assert histogram("aa aa aa aa") == {"a": 4}
    assert histogram("aa aa aa a") == {"a": 4, " ": 1}
    assert histogram("a