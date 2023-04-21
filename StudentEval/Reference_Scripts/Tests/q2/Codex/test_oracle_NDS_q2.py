"""
Given a month and a list of possible birthdays, returns True if there is only one possible birthday with that month and unique day, False otherwise. 
Implement 3 different functions: unique_day, unique_month and contains_unique_day.
"""


def unique_day(day, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if birthday[1] == day:
            count += 1
    return count == 1


def unique_month(month, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if birthday[0] == month:
            count += 1
    return count == 1


def contains_unique_day(month, possible_birthdays):
    for birthday in possible_birthdays:
        if birthday[0] == month and unique_day(birthday[1], possible_birthdays):
            return True
    return False

def test():
    unique_day(1,
        [(1, 1, 1),
         (2, 2, 2),
         (3, 3, 3)]) == True
    assert unique_day(2,
        [(1, 1, 1),
         (2, 2, 2),
         (3, 3, 3)]) == True
    assert unique_day(3,
        [(1, 1, 1),
         (2, 2, 2),
         (3, 3, 3)]) == True
    assert unique_day(4,
        [(1, 1, 1),
         (2, 2, 2),
         (3, 3, 3)]) == False
    assert unique_day(5,
        [(1, 1, 1),
         (2, 2, 2),
         (3, 3, 3)]) == False
    assert unique_month(1, [(1, 2, 3), (4, 5, 6), (7, 8, 9)]) == True
    assert unique_month(1, [(4, 5, 6), (4, 5, 6), (4, 5, 6)]) == False
    assert contains_unique_day(1, [[(1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)],
                     [(1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)]]) == True