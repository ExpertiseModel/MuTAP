def generate_test_case():
    import random
    possible_birthdays = []
    for i in range(100):
        possible_birthdays.append((random.randint(1, 12), random.randint(1, 31)))
    month = random.randint(1, 12)
    return month, possible_birthdays


# test the function above

def test_contains_unique_day():
    month, possible_birthdays = generate_test_case()
    print(contains_unique_day(month, possible_birthdays))

