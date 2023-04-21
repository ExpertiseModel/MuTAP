from script_74_cp_few_shot import total_match


def test_total_match():
    assert total_match(['a', 'b', 'c'], ['aa', 'bb', 'cc']) == ['a', 'b', 'c']
    assert total_match(['aa', 'bb', 'cc'], ['a', 'b', 'c']) == ['a', 'b', 'c']
    assert total_match(['aa', 'bb', 'cc'], ['aaa', 'bbb', 'ccc']) == ['aa', 'bb', 'cc']
    assert total_match(['aaa', 'bbb', 'ccc'], ['aa', 'bb', 'cc']) == ['aa', 'bb', 'cc']
    assert total_match(['aa', 'bb', 'cc'], ['aaa', 'bbb']) == ['aa', 'bb', 'cc']
    assert total_match(['aaa', 'bbb'], ['aa', 'bb', 'cc']) == ['aa', 'bb', 'cc']
    assert total_match(['aa', 'bb', 'cc'], ['aaa', 'bbb', 'ccc', 'dddd']) == ['aa', 'bb', 'cc']
    assert total_match(['aaa', 'bbb', 'ccc', 'dddd'], ['aa', 'bb', 'cc']) == ['aa', 'bb', 'cc']
    assert total_match(['aa', 'bb', 'cc'], ['aaa', 'bbb', 'ccc', 'dddd', 'eeeee']) == ['aa', 'bb', 'cc']
    assert total_match(['aaa', 'bbb', 'ccc', 'dddd', 'eeeee'], ['aa', 'bb', 'cc']) == ['aa', 'bb', 'cc']
    assert total_match(['aa', 'bb', 'cc'], ['aaa', 'bbb', 'ccc', 'dddd', 'eeeee', 'ffffff']) == ['aa', 'bb', 'cc']
    assert total_match(['aaa', 'bbb', 'ccc', 'dddd', 'eeeee', 'ffffff'], ['aa', 'bb', 'cc']) == ['aa', 'bb', 'cc']
    assert total_match(['aa', 'bb', 'cc'], ['aaa', 'bbb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg']) == ['aa', 'bb', 'cc']


