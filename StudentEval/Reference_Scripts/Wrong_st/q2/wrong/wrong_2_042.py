def unique_day(day, possible_birthdays):
    days = ()
    for birthdays in possible_birthdays:
        days += (birthdays[1],)
    a = 0
    for dates in days:
        if day == dates:
            a +=1
    if a !=1:
        return False
    return True

def unique_month(month, possible_birthdays):
    months = ()
    for birthdays in possible_birthdays:
        months += (birthdays[0],)
    a = 0
    for dates in months:
        if month == dates:
            a +=1
    if a !=1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    return 
