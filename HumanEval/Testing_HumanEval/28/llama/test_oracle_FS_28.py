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



#</testCase>


#<testCase>

    assert concatenate(["hello", "world"]) == "hellogworld"



#</testCase>


#<testCase>

    assert concatenate(["hello", "world", " again"]) == "hellogworldagain"



#</testCase>


#<testCase>
    assert concatenate(["hello", 42, "world"]) == "42hellogworld"



#</testCase>


#<testCase>


