def unique_day(day, possible_birthdays):
    days = ()
    unique = ()
    for i in possible_birthdays:
        days += (i[1],)
    for i in days:
        if i == day:
            unique += (i,)
        else:
            continue
    if len(unique) == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    months = ()
    unique = ()
    for i in possible_birthdays:
        months += (i[0],)
    for i in months:
        if i == month:
            unique += (i,)
        else:
            continue
    if len(unique) == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    return 
