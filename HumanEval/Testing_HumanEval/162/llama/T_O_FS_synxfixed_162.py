def string_to_md5(text):
    
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None


#</code>
#<test>
def test():
   
    assert string_to_md5("") is None


    assert string_to_md5("hello") == "73ef8e88b92a4a65b231a9418c96a1425"

    assert string_to_md5("Hello World! How are you today?") == "73ef8e88b92a4a65b231a9418c96a1425"

    assert string_to_md5("This is an ASCII text") == "73ef8e88b92a4a65b231a9418c96a1425"