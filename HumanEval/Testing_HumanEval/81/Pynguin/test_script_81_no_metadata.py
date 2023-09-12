import script_81 as module_0


def test_case_0():
    bytes_0 = b"D\x00\xe8'\xff4\xfa.\x82"
    var_0 = module_0.numerical_letter_grade(bytes_0)



def test_case_2():
    bytes_0 = b"q\x02\x9ed\x9c{3\x04\x16F\xe3\xadh\xa0\xb3\xa8\x7f\xfa\xa0\x0c"
    var_0 = module_0.numerical_letter_grade(bytes_0)


def test_case_3():
    bytes_0 = b"q\x02\x9ed\x9c{\x16F\xe3\xadh\xa0\xb3\xa8\x7f\xfa\xa0\x0c"
    var_0 = module_0.numerical_letter_grade(bytes_0)


def test_case_4():
    bytes_0 = b"\xc8\xd0\x91\xe9\x06\x01\xae3\x08"
    var_0 = module_0.numerical_letter_grade(bytes_0)


def test_case_5():
    bytes_0 = b"=\x03n\x88\xab-\xd8Y9$p\x9d\xf1\x9dC\x91\xcb\x0e"
    var_0 = module_0.numerical_letter_grade(bytes_0)