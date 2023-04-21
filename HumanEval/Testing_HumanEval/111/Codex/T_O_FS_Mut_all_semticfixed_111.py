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
    assert histogram("a thr rockson land") == {'a': 1, 'thr': 1, 'rockson': 1, 'land': 1}
    assert histogram("a a a a  b c d a a") == {'a': 6}
    assert histogram("an ant str") == {'an': 1, 'ant': 1, 'str': 1}
    assert histogram("an ant ant") == {'ant': 2}
    assert histogram("") == {}
    assert histogram("a") == {'a': 1}
    assert histogram("a a") == {'a': 2}
    assert histogram("tricky") == {'tricky': 1}
    assert histogram("e e e e") == {"e": 4}
    assert histogram("aa aa aa aa") == {'aa': 4}
    assert histogram("aa aa aa a") == {'aa': 3}
