#https://rosettacode.org/wiki/Find_the_last_Sunday_of_each_month#Python
import sys
import calendar

year = 2018
if len(sys.argv) > 1:
    try:
        year = int(sys.argv[-1])
    except ValueError:
        pass

for month in range(1, 13):
    last_tuesday = max(week[-6] for week in calendar.monthcalendar(year, month))
    print('{}-{}-{:2}'.format(year, calendar.month_abbr[month], last_tuesday))
