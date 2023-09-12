[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def split_words(txt):
    
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',',' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])

# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `split_words` function:
```Python
def test_single_word():
    txt = "hello"
    assert split_words(txt) == [\"hello\"]

def test_spaces():
    txt = "hello world"
    assert split_words(txt) == [\"hello\", \"world\"]

def test_commas():
    txt = ",hello,world,"
    assert split_words(txt) == [\"hello\", \"world\"]

def test_mixed():
    txt = "hello,world,foo,bar"
    assert split_words(txt) == [\"hello\", \"world\", \"foo\", \"bar\"]

def test_lowercase():
    txt = "heLlO WoRlD"
    assert split_words(txt) == [\"hello\", \"world\"]

def test_digits():
    txt = "1hello23world"
    assert split_words(txt) == [\"1\", \"hello\", \"2\", \"world\"]

def test_special_chars