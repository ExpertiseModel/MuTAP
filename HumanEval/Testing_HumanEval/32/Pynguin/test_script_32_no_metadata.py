import pytest
import script_32 as module_0


def test_case_0():
    float_0 = 3523.15246
    list_0 = [float_0, float_0]
    var_0 = module_0.find_zero(list_0)
    assert var_0 == pytest.approx(-1.0, abs=0.01, rel=0.01)


def test_case_1():
    dict_0 = {}
    var_0 = module_0.find_zero(dict_0)
    assert var_0 == pytest.approx(-1.0, abs=0.01, rel=0.01)


def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.find_zero(list_0)
    assert var_0 == pytest.approx(-1.0, abs=0.01, rel=0.01)
    var_1 = module_0.find_zero(list_0)
    assert var_1 == pytest.approx(-1.0, abs=0.01, rel=0.01)


def test_case_3():
    bool_0 = False
    float_0 = -3160.521785
    list_0 = [bool_0, float_0]
    var_0 = module_0.find_zero(list_0)
    assert var_0 == pytest.approx(-5.820766091346741e-11, abs=0.01, rel=0.01)


def test_case_4():
    list_0 = []
    bytes_0 = b"\xb2\x98\x04\x1fC\x9d\xad\x1a\xe8\xabz\x10<\x86\xeai\x95\xe4\x1a"
    var_0 = module_0.poly(list_0, bytes_0)
    assert var_0 == 0
    var_1 = module_0.find_zero(bytes_0)
    assert var_1 == pytest.approx(-1.1777043586480431, abs=0.01, rel=0.01)
