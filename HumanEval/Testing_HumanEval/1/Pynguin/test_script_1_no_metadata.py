# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import script_1 as module_0


def test_case_0():
    str_0 = "+T&>>'DIZ(tbUDKQxjC1"
    list_0 = module_0.separate_paren_groups(str_0)
    list_1 = module_0.separate_paren_groups(str_0)
    list_2 = module_0.separate_paren_groups(str_0)
    str_1 = '=gg&l34[JFYX(y'
    list_3 = module_0.separate_paren_groups(str_1)


def test_case_1():
    str_0 = 'U)'
    list_0 = module_0.separate_paren_groups(str_0)
    assert list_0 == []
    str_1 = 'voo'
    list_1 = module_0.separate_paren_groups(str_1)


def test_case_2():
    str_0 = ']UBq,]R'
    str_1 = 'M\\Ms^\t'
    list_0 = module_0.separate_paren_groups(str_1)
    list_1 = module_0.separate_paren_groups(str_1)
    list_2 = module_0.separate_paren_groups(str_0)
    list_3 = module_0.separate_paren_groups(str_0)
    list_4 = module_0.separate_paren_groups(str_1)
    list_5 = module_0.separate_paren_groups(str_1)
    list_6 = module_0.separate_paren_groups(str_1)
    str_2 = 'r_t(U\x0b)7\t\x0b|Fg#,'
    list_7 = module_0.separate_paren_groups(str_2)
    assert list_7 == ['()']
    list_8 = module_0.separate_paren_groups(str_0)
    list_9 = module_0.separate_paren_groups(str_0)
    list_10 = module_0.separate_paren_groups(str_0)
    str_3 = '&GnDiYM'
    list_11 = module_0.separate_paren_groups(str_3)
    str_4 = 'N4u#V80%(5q'
    list_12 = module_0.separate_paren_groups(str_4)
    str_5 = '#uUzvxJ5:P$E<r#5O'
    str_6 = '!'
    list_13 = module_0.separate_paren_groups(str_6)
    list_14 = module_0.separate_paren_groups(str_5)
    list_15 = module_0.separate_paren_groups(str_3)
    list_16 = module_0.separate_paren_groups(str_5)
    str_7 = '*+IF\tA'
    list_17 = module_0.separate_paren_groups(str_7)
    list_18 = module_0.separate_paren_groups(str_7)
    list_19 = module_0.separate_paren_groups(str_3)
    list_20 = module_0.separate_paren_groups(str_0)
    str_8 = '"RYbC+,]\''
    list_21 = module_0.separate_paren_groups(str_8)
    str_9 = 'zbZT7;\\2/p"cRB\x0b{[[K>'
    list_22 = module_0.separate_paren_groups(str_9)
    list_23 = module_0.separate_paren_groups(str_0)
