# Automatically generated by Pynguin.
import script_73 as module_0


def test_case_0():
    dict_0 = {}
    list_0 = [dict_0, dict_0]
    var_0 = module_0.smallest_change(list_0)
    assert var_0 == 0
    tuple_0 = ()
    var_1 = module_0.smallest_change(tuple_0)
    assert var_1 == 0


def test_case_1():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    var_0 = module_0.smallest_change(set_0)
    assert var_0 == 0