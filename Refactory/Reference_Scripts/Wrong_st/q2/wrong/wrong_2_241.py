def unique_day(day, possible_birthdays):
    days = ()
    for i in possible_birthdays:
        days += (i[1],)
    count = 0
    for ele in days:
        if ele == day:
            count += 1
    if count == 1:
        return True
    else:
        return False
