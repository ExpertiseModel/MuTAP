[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def string_to_md5(text):
    
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None


# test case
def test():
    assert [/INST]  Here are some test cases for the `string_to_md5` function:
```
def test_empty_string():
    assert string_to_md5("") is None

def test_short_string():
    assert string_to_md5("hello") == "3021702630235511329"

def test_long_string():
    assert string_to_md5("The quick brown fox jumped over the lazy dog.") == "66639754132305921932"

def test_unicode_string():
    assert string_to_md5("😊").startswith("a3")

def test_invalid_encoding():
    with pytest.raises(ValueError):
        string_to_md5("hello".encode("utf-16"))

def test_empty_bytes():
    assert string_to_md5(b"").startswith("00")

def test_non_ascii_bytes():
    with pytest.raises