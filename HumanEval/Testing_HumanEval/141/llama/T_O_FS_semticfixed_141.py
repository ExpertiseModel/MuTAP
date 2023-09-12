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


#</original code>


#<test>

def test():
    assert file_name_check("file1.txt") == "Yes"
    assert file_name_check("file2.exe") == "Yes"
    assert file_name_check("file3.dll") == "Yes"
    assert file_name_check("file4.txt") == "Yes"
    assert file_name_check("file5.file") == "No"
    assert file_name_check("file6.txt.exe") == "No"
    assert file_name_check("file7.txt.dll") == "No"
