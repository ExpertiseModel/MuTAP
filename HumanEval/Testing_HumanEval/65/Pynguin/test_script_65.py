# Automatically generated by Pynguin.
# Automatically generated by Pynguin.
import pytest
import script_65 as module_0


def test_case_0():
    int_0 = 63
    none_type_0 = None
    var_0 = module_0.circular_shift(int_0, int_0)
    assert var_0 == "36"
    var_1 = module_0.circular_shift(none_type_0, int_0)
    assert var_1 == "enoN"
    var_2 = module_0.circular_shift(int_0, int_0)
    assert var_2 == "36"


def test_case_1():
    bool_0 = False
    var_0 = module_0.circular_shift(bool_0, bool_0)
    assert var_0 == "False"
    none_type_0 = None
    var_1 = module_0.circular_shift(none_type_0, bool_0)
    assert var_1 == "None"
    var_2 = module_0.circular_shift(bool_0, bool_0)
    assert var_2 == "False"
    var_3 = module_0.circular_shift(bool_0, bool_0)
    assert var_3 == "False"
   

