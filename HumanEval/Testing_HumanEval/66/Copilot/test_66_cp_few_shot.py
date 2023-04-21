from script_66_cp_few_shot import digitSum


def test_digitSum():
    assert digitSum("") == 0
    assert digitSum("a") == 0
    assert digitSum("A") == 65
    assert digitSum("aA") == 65
    assert digitSum("Aa") == 65
    assert digitSum("AaBbCc") == 195
    assert digitSum("AaBbCcDdEe") == 390
    assert digitSum("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 2015
    assert digitSum("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") == 2015
    assert digitSum("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789") == 2015


