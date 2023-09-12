def decimal_to_binary(decimal):
    
    return "db" + bin(decimal)[2:] + "db"


#</code>
#<test>
def test():
  
    assert decimal_to_binary(1) == "db10"

    assert decimal_to_binary(-1) == "db10"

    assert decimal_to_binary(12) == "db110"

    assert decimal_to_binary(-12) == "db110"

    assert decimal_to_binary(123) == "db11011"

    assert decimal_to_binary(-123) == "db11011"