def valid_date(date):
    
    try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month < 1 or month > 12:
            return False
        if month in [1,3,5,7,8,10,12] and day < 1 or day > 31:
            return False
        if month in [4,6,9,11] and day < 1 or day > 30:
            return False
        if month == 2 and day < 1 or day > 29:
            return False
    except:
        return False

    return True


# test case

def test():
    assert valid_date("2022-01-01") == False

    assert valid_date("01-01-2022") == True

    assert valid_date("abc-01-2022") == False

    assert valid_date("2022-13-01") == False

    assert valid_date("2022-01-aaa") == False
    assert valid_date("2022-12-31") == False
    assert valid_date("2022-01-01") == True

    # Test with an invalid date
    assert valid_date("abc-01-2022") == False

    # Test with a date in an invalid format
    assert valid_date("2022-aaa-01") == False

    # Test with a date that exceeds the range of valid dates
    assert valid_date("2022-01-32") == False

    # Test with a date that is greater than the maximum allowed value
    assert valid_date("2022-01-max") == False
    assert valid_date("2022-01-01") == True

    # Mutant case: test the function with an invalid month input
    assert valid_date("abc-01-2022") == False

    # Mutant case: test the function with an invalid day input
    assert valid_date("2022-13-01") == False

    # Mutant case: test the function with an invalid year input
    assert valid_date("2022-01-aaa") == False
    assert valid_date("2022-01-01") == True
    # Test the modified function with a date in the mutated block
    assert valid_date("01-01-2022") == True
    # Test the modified function with a date beyond the mutated block
    assert valid_date("2022-31-01") == False
    assert valid_date("2022-02-30") == False

    # Test for incorrect day validation in month 4
    assert valid_date("2022-04-31") == False

    # Test for incorrect day validation in month 6
    assert valid_date("2022-06-30") == False

    # Test for incorrect day validation in month 9
    assert valid_date("2022-09-31") == False

    # Test for incorrect day validation in month 11
    assert valid_date("2022-11-30") == False

    # Test for correct day validation in month 2
    assert valid_date("2022-02-29") == True
    assert valid_date("abc-13-2022") == False
    assert valid_date("2022-13-01") == False
    assert valid_date("abc-01-2022") == True

    # Test with a bad day value
    assert valid_date("2022-13-golf") == True

    # Test with a bad year value
    assert valid_date("abc-01-13") == True

    # Test with a valid date
    assert valid_date("2022-01-01") == True
    assert valid_date("2022-01-01") == True

    # Test the edge case where the month is 2 and the day is 29 or 30
    assert valid_date("2022-02-29") == False
    assert valid_date("2022-02-30") == False

    # Test the edge case where the month is 2 and the day is 1
    assert valid_date("2022-02-01") == False
    assert valid_date("2022-02-30") == False
    assert valid_date("2022-02-29") == True
    assert valid_date("2022-01-01") == True

    assert valid_date("01-01-2022") == False

    assert valid_date("abc-01-2022") == False

    assert valid_date("2022-13-01") == False

    assert valid_date("2022-01-aaa") == False
    assert valid_date("02-30-2022") == False

    assert valid_date("31-01-2022") == False




