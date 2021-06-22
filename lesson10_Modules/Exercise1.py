import calendar
import datetime

def year_is_leap(year):
    return calendar.isleap(year)

year = 2010
print(year, "is leap year" if year_is_leap(year) else "is not leap year")

year = 2020
print(year, "is leap year" if year_is_leap(year) else "is not leap year")

first_year = 2020
last_year = 2080
sum = 0
while first_year <= last_year:
    if year_is_leap(first_year):
        sum = sum + 1
    first_year += 1
first_year = 2020
print("There is", sum, "leap years between", first_year, "and", last_year)

#today = datetime.datetime.today()
#print(datetime.datetime.today().weekday())