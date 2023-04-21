from script_28_cp_few_shot import concatenate


def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate(['a', 'b', 'c', 'd', 'e', 'f']) == 'abcdef'
    assert concatenate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 'abcdefghij'




