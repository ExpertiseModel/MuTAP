from script_4_cp_few_shot import mean_absolute_deviation

def test_mean_absolute_deviation():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) == 1.0
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) == 1.5
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]) == 2.0
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]) == 2.5
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]) == 3.0
