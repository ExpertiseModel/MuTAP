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

    assert histogram("hello world") == {'hello': 1, 'world': 1}

    assert histogram("this is a very long string with many characters") == {'this': 1, 'is': 1, 'a': 1, 'very': 1, 'long': 1, 'string': 1, 'with': 1, 'many': 1, 'characters': 1}
