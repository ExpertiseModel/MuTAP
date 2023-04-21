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
    histogram("one one") == {"one": 2}
    assert histogram("one two three four five six seven eight") == {"one": 1, "two": 1, "three": 1, "four": 1, "five": 1, "six": 1, "seven": 1, "eight": 1}
    compare(histogram("one two three four five six seven eight"), {' one': 1, ' two': 1, ' three': 1, ' four': 1, ' five': 1, ' six': 1, ' seven': 1, ' eight': 1})

test()
