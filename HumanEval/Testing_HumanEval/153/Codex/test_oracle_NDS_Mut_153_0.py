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
    assert Strongest_Extension("Hello", ["lloHe", "Hello", "helle"]) == "Hello.lloHe"
    assert Strongest_Extension("Hello", ["Hllo", "Hello", "loHel"]) == "Hello.Hllo"
    assert Strongest_Extension("Hello", ["Hello", "hll", "el"]) == "Hello.el"
    assert Strongest_Extension("Hello", ["loHel", "Hllo", "Hello"]) == "Hello.Hllo"
    assert Strongest_Extension("Hello", ["llo", "Hllo", "Hello"]) == "Hello.Hllo"

