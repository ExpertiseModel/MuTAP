def decimal_to_binary(decimal):
    
    return "db" + bin(decimal)[2:] + "db"


#</code>
#<test>

def test():
    assert decimal_to_binary(1) == "db1db"

    assert decimal_to_binary(-1) == "dbb1db"

    assert decimal_to_binary(12) == "db1100db"

    assert decimal_to_binary(-12) == "dbb1100db"

    assert decimal_to_binary(123) == "db1111011db"

    assert decimal_to_binary(-123) == "dbb1111011db"
