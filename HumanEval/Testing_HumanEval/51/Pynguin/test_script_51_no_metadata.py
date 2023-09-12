import pytest
import script_NDS_51 as module_0


def test_case_1():
    bytes_0 = b""
    var_0 = module_0.remove_vowels(bytes_0)
    assert var_0 == ""
    var_1 = module_0.remove_vowels(var_0)
    assert var_1 == ""
    var_2 = module_0.remove_vowels(bytes_0)
    assert var_2 == ""
   


def test_case_3():
    str_0 = "\rQl"
    var_0 = module_0.remove_vowels(str_0)
    assert var_0 == "\rQl"
    list_0 = []
    var_1 = module_0.remove_vowels(list_0)
    assert var_1 == ""
    var_2 = module_0.remove_vowels(list_0)
    assert var_2 == ""
    

def test_case_4():
    str_0 = ":$31A"
    var_0 = module_0.remove_vowels(str_0)
    assert var_0 == ":$31"
    
