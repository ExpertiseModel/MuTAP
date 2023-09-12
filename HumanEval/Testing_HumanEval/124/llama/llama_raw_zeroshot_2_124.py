[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
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
    assert [/INST]  Sure! Here are some test cases for the `valid_date` function:
```
def test_valid_date_empty_string():
    assert not valid_date("")

def test_valid_date_bad_format():
    assert not valid_date("03-aaa-2000")

def test_ invalid_month():
    assert not valid_date("03-11-2000")

def test_invalid_day():
    assert not valid_date("03-11-2000")

def test_invalid_year():
    assert not valid_date("03-11-99")

def test_ valid_date():
    assert valid_date("03-11-2000")

def test_ invalid_month_range():
    assert not valid_date("03-20-2000")

def test_ invalid_day_range():
    assert not valid_date("03-11-2000")

def test_ too_far_in_future():
