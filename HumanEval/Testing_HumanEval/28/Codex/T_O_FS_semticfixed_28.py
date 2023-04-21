from typing import List


def concatenate(strings: List[str]) -> str:
    
    return ''.join(strings)




def test():
    assert concatenate(["first", "second", "third"]) == "firstsecondthird"
    assert concatenate(["first", "second", "third"]) == "firstsecondthird"
    assert concatenate(["", "", ""]) == ""
    assert concatenate(["", "", ""]) == ""
