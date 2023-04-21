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
    assert file_name_check('ex.txt') == 'Yes'
    assert file_name_check('exe.txt') == 'Yes'
    assert file_name_check('something.doc') == 'No'
    assert file_name_check('DOC.DOC') == 'No'
    assert file_name_check('no.') == 'No'
    assert file_name_check('no.ext') == 'No'
    assert file_name_check('no.extent') == 'No'
    assert file_name_check('') == 'No'
    assert file_name_check('1.txt') == 'No'
    assert file_name_check('no.1') == 'No'
