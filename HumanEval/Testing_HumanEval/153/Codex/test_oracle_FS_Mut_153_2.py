def Strongest_Extension(class_name, extensions):
    
    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans




def test():
    Strongest_Extension("a","")
# solution
def test():
    assert Strongest_Extension("a","b") == "a.b"
    assert Strongest_Extension("a","B") == "a.B"
    assert Strongest_Extension("a","Bb") == "a.Bb"
    assert Strongest_Extension("a","BbB") == "a.BbB"
    assert Strongest_Extension("a","BbBb") == "a.BbBb"
    assert Strongest_Extension("a","BBbbb") == "a.BBbbb"
    assert Strongest_Extension("a","BBBBBB") == "a.BBBBBB"
    assert Strongest_Extension("a","BBbbbB") == "a.BBbbbB"
    assert Strongest