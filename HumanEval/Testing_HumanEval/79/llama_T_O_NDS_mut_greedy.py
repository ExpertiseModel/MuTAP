def decimal_to_binary(decimal):
    
    return "db" + bin(decimal)[2:] + "db"
assert decimal_to_binary(0) == "db0db"
