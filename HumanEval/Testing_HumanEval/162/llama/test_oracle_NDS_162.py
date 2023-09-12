def string_to_md5(text):
    
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None


# test case
def test():
   
    assert string_to_md5("") == None

    assert string_to_md5("hello") == "3021702630235511329"


    assert string_to_md5("The quick brown fox jumped over the lazy dog.") == "66639754132305921932"

    assert string_to_md5("😊").startswith("a3")

    assert string_to_md5(b"").startswith("00")

