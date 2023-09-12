def file_name_check(file_name):
    
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if not lst[1] in suf:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'


# test case

def test():
    # Test with valid file name
    assert file_name_check("example.txt") == "Yes", "File name should be valid"
    # Test with invalid file name
    assert file_name_check("example. ABC") == "No", "File name should not contain non-alpha characters"
    # Test with file name with illegal characters
    assert file_name_check("example.txt\0") == "No", "File name should not contain null characters"
    # Test with file name with illegal extensions
    assert file_name_check("example.txt ABC") == "No", "File name should not have illegal extensions"
    # Test with file name with length > 3
    assert file_name_check("example.txt ABC") == "No", "File name should not have length > 3"
    assert file_name_check("example.txt\0abc") == "No", "File name should not contain illegal characters"
    # Test with a modified file name that has an extra extension
    assert file_name_check("example.txtabc") == "No", "File name should not have extra extensions"
    # Test with a modified file name that has an illegal suffix
    assert file_name_check("example.txtabc.dz") == "No", "File name should not have illegal suffix"
    assert file_name_check("") == "Yes", "File name should be valid"
