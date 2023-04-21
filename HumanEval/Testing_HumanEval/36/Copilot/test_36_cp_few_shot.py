from script_36_cp_few_shot import fizz_buzz



def test_fizz_buzz():
    assert fizz_buzz(0) == 0
    assert fizz_buzz(1) == 0
    assert fizz_buzz(2) == 0
    assert fizz_buzz(3) == 0
    assert fizz_buzz(4) == 0
    assert fizz_buzz(5) == 0
    assert fizz_buzz(6) == 0
    assert fizz_buzz(7) == 0
    assert fizz_buzz(8) == 0
    assert fizz_buzz(9) == 0
    assert fizz_buzz(100) == 4
    assert fizz_buzz(1000) == 40
    assert fizz_buzz(10000) == 400
    assert fizz_buzz(100000) == 4000

