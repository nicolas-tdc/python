"""Leap year"""

def leap_year(year):
    """
    :param year: int
    :return: bool
    Return True if year is a leap year
    """
    if ( year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
        return True
    else:
        return False
