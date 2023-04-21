from script_46_cp_few_shot import fib4


def test_fib4():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 2
    assert fib4(5) == 4
    assert fib4(6) == 6
    assert fib4(7) == 8
    assert fib4(8) == 10
    assert fib4(9) == 14
    assert fib4(10) == 18
    assert fib4(11) == 26
    assert fib4(12) == 34
    assert fib4(13) == 50
    assert fib4(14) == 68
    assert fib4(15) == 98
    assert fib4(16) == 138
    assert fib4(17) == 198
    assert fib4(18) == 278
    assert fib4(19) == 398
    assert fib4(20) == 558


