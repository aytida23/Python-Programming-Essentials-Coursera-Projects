"""
Implementing the datetime module and computing simple processing on
dates using the Python's datetime module.
"""

import datetime

#days in month function
def days_in_month(year, month):
    """
    This function takes two integers: a year and a month that return the number
    of days in that given month.
    """

    #computing number of days in a month
    if (datetime.MINYEAR <= year <= datetime.MAXYEAR) and (1 <= month <=11):
        date1 = datetime.date(year,month,1)
        date2 = datetime.date(year,month+1,1)
        return (date2 - date1).days
    elif (datetime.MINYEAR <= year <= datetime.MAXYEAR) and (month == 12):
        date1 = datetime.date(year,month,1)
        date2 = datetime.date(year+1,1,1)
        return (date2 - date1).days
    else:
        return False
    


#date is valid function
def is_valid_date(year, month, day):
    """
    This function takes three integers: a year, a month, and a day. and return
    True if the date is valid and False otherwise.
    """

    #computing date is valid or not
    days = days_in_month(year, month)
    if ((datetime.MINYEAR <= year <= datetime.MAXYEAR) and (1<= month <= 12) and (0 < day <= days)):
        return True
    else:
        return False


#computing number of days between two dates
def days_between(year1, month1, day1, year2, month2, day2):
    """
    Takes six integers (year1, month1, day1, year2, month2, day2) and returns
    the number of days from an earlier to a later date and if either date is
    invalid the function return 0.
    """

    #computing the number between days
    #conditions and computation of days between two dates
    if (is_valid_date(year1, month1, day1)) and (is_valid_date(year2, month2, day2)):

        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)

        if (date2 > date1):
            number_of_days = date2 - date1
            return number_of_days.days
        else:
            return 0
    else:
        return 0
    

#computing person's age in days
def age_in_days(year, month, day):
    """
    Takes three integers as input(year,month,day) of a persons
    birthday and return that person's age in days as of today.
    """
    
    #conditions and calculations of person's age in days
    
    if (is_valid_date(year, month, day)):
        today = datetime.date.today()
        person_bday = datetime.date(year, month, day)
        if (person_bday < today):
            person_age_in_days = days_between(year, month, day, today.year, today.month, today.day)
            return person_age_in_days
        else:
            return 0
    else:
        return 0
    


