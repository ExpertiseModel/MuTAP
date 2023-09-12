[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
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



# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `Strongest_Extension` function:
```
test_cases = [
    # Test case 1: Single extension
    {
        'class_name': 'Person',
        'extensions': ['John', 'Mike', 'Jane'],
        'expected': 'Person.John'
    },

    # Test case 2: Same extension multiple times
    {
        'class_name': 'City',
        'extensions': ['New York', 'New York', 'Los Angeles'],
        'expected': 'City.New York'
    },

    # Test case 3: Uppercase and lowercase letters
    {
        'class_name': 'Email',
        'extensions': ['john@example.com', 'john@example.com', 'MIKE@example.com'],
        'expected': 'Email.john@example.com'
    },

    # Test case 4: Multi-word extension
    {
        'class_name': 'Name',
        'extensions': ['John Doe', 'Jane Smith', 'John Doe