def string_to_md5(text):
    
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None


#</code>
#<test>

def test():
    assert string_to_md5("") is None


    assert string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"

    assert string_to_md5("Hello World! How are you today?") == "635479220be3f4d871bd89824583bf88"

    assert string_to_md5("This is an ASCII text") == "4acaae25c8a33e1b6adcc4aa6a327dd6"
