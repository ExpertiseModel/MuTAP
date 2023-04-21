

def unique_month(month, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if birthday[0] == month:
            count += 1
    return count == 1


def test():
    unique_month(1, [(1, 2, 3), (4, 5, 6), (7, 8, 9)]) == True
    assert 
    unique_month(1, [(4, 5, 6), (4, 5, 6), (4, 5, 6)]) == False
    print("All tests passed!")


test()
