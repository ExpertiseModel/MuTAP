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




def test():
    assert "No" == file_name_check('1.exe')
    assert "No" == file_name_check('1.aaaaa')
    assert "Yes" == file_name_check('abc.txt')
    assert "Yes" == "Yes"
    assert file_name_check('abc')== "No" 
    assert file_name_check('')== "No" 
    assert file_name_check(None) == "No"    
    assert file_name_check('1.exe') == "No"
    assert file_name_check('1.aaaaa')== "No"
    assert file_name_check('abc.txt')== "Yes" 
