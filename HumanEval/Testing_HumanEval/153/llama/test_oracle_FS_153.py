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
   
 
    assert Strongest_Extension("", []) == ""


    assert Strongest_Extension("", ["a"]) == "a"


    assert Strongest_Extension("", ["ä"]) == "ä"


    assert Strongest_Extension("", ["A", "a"]) == "A"


    assert Strongest_Extension("", ["a", "b", "c", "d", "e", "f"]) == "ef"

    extensions = [""]
    ans = Strongest_Extension("", [""])
