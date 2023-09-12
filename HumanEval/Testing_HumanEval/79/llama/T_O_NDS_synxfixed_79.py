
def decimal_to_binary(decimal):
    
    return "db" + bin(decimal)[2:] + "db"


# test case
def test():
   
    assert decimal_to_binary(0) == "db0000000"

    assert decimal_to_binary(123) == "db1100111"

    assert decimal_to_binary(-123) == "db1110100"

    assert decimal_to_binary(-6) == "db1100111"
 