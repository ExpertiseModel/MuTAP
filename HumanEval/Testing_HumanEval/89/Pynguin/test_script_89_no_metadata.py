# Automatically generated by Pynguin.
import script_89 as module_0



def test_case_1():
    bytes_0 = b""
    var_0 = module_0.encrypt(bytes_0)
    assert var_0 == ""
    var_1 = module_0.encrypt(var_0)
    assert var_1 == ""
    var_2 = module_0.encrypt(bytes_0)
    assert var_2 == ""
    


def test_case_3():
    str_0 = "\rQl"
    var_0 = module_0.encrypt(str_0)
    assert var_0 == "\rQp"
    list_0 = []
    var_1 = module_0.encrypt(list_0)
    assert var_1 == ""
    var_2 = module_0.encrypt(list_0)
    assert var_2 == ""
    