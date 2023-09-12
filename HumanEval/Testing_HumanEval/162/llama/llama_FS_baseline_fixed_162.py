def string_to_md5(text):
    
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None


#</code>
#<test>

def test():
    assert string_to_md5("") is None
