import sys

locations = sys.path

for i in locations:
    print(i)

import calendar

leapdays = calendar.leapdays(2000, 2050)
print(leapdays)

is_it_leap = calendar.month(themonth=12, theyear=2013)
print(is_it_leap)
