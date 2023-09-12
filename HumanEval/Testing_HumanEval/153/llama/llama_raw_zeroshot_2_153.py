[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans



# test case
def test():
    assert [/INST]  Sure, I can generate test cases for the `StrongestExtension` function! Here are some examples:
```python
test_cases = []
# class name and extensions list
test_cases.append([
    "Slices",
    ["SErviNGSliCes", "Cheese", "StuFfed"]
])
# class name and extensions list
test_cases.append([
    "my_class",
    ["AA", "Be", "CC"]
])
# empty list of extensions
test_cases.append([
    "Slices",
    []
])

# single extension list
test_cases.append([
    "Slices",
    ["SErviNGSliCes"]
])
# multiple extensions with same strength
test_cases.append([
    "my_class",
    ["AA", "Be", "AA"]
])

# extra uppercase letter in extension
test_cases.append([
    "my_class",
    ["Aa", "Be", "CC"]
])
# extra lowercase letter in extension
test_cases.append([
   