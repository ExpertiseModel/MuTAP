def correct_bracketing(brackets: str):
    
    depth = 0
    for b in brackets:
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0




#</code>
#<test>
def test():
   
    assert correct_bracketing("< ABC >") == True
    assert correct_bracketing("ABC <") == True
    assert correct_bracketing(" ABC <") == False
    assert correct_bracketing("</ABC>") == True
    assert correct_bracketing(" > ABC</") == False
    assert correct_bracketing(" ABC />") == False
    assert correct_bracketing(" ABC < >") == False

#</test>













