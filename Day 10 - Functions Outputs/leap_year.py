def is_leap_year(year):
    """Check if input is leap year"""
    int(year)
    leap_year = False
    if (year % 4) == 0:
        leap_year = True
        if (year % 100) == 0:
            leap_year = False
        if (year % 400) == 0:
            leap_year = True
    return leap_year

print (is_leap_year(2000))

