def unique_day(day, possible_birthdays):
    result = ()
    for p in possible_birthdays:
        pd = p[1]
        if day == pd:
            result = result + (day,)
    if len(result) > 1:
        return False
    return True

def unique_month(month, possible_birthdays):
    result = ()
    for p in possible_birthdays:
        pm = p[0]
        if month == pm:
            result = result + (month,)
    if len(result) > 1:
        return False
    return True
    
    
def contains_unique_day(month, possible_birthdays):
    return 
