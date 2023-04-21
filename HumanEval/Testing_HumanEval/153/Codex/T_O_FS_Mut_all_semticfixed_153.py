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
    assert Strongest_Extension("a", "b") == "a.b"   
    assert Strongest_Extension("a", ["b"]) == "a.b"
    assert Strongest_Extension("a","b") == "a.b"
    assert Strongest_Extension("a","B") == "a.B"
    assert Strongest_Extension("a","Bb") == "a.B"
    assert Strongest_Extension("a","BbB") == "a.B"
    assert Strongest_Extension("a","BbBb") == "a.B"
    assert Strongest_Extension("a","BBbbb") == "a.B"
    assert Strongest_Extension("a","BBBBBB") == "a.B"
    assert Strongest_Extension("a","BBbbbB") == "a.B"
    assert Strongest_Extension("a","b") == "a.b"
    assert Strongest_Extension("b","b") == "b.b"
    assert Strongest_Extension("b","a") == "b.a"
    assert Strongest_Extension("","1") == ".1"     
    assert Strongest_Extension("1","1") == "1.1"
    assert Strongest_Extension("1","a") == "1.a"



