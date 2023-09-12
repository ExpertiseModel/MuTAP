from typing import List


def concatenate(strings: List[str]) -> str:
    
    return ''.join(strings)




#</code>
#<test>

def test():
    #<testCase>

    assert concatenate([]) == ""


#</testCase>


#<testCase>
    assert concatenate(['hello']) == "hello"



    assert concatenate(["hello", "world"]) == "helloworld"



#</testCase>


#<testCase>

    assert concatenate(["hello", "world", " again"]) == "helloworld again"



#</testCase>


#<testCase>
    assert concatenate(["hello", 42, "world"]) == "42hellogworld"


#</testCase>


#<testCase>



