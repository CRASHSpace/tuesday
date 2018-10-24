import datetime
import dateutil.parser

date = datetime.datetime.today()

def is_it_tuesday(date_to_check):
  if date_to_check.weekday() == 1:
    print("yes")
  else:
    print("no")

if __name__ == "__main__":
    raw_date_string = input('What day do you want to check? ')
    checkme = dateutil.parser.parse(raw_date_string)
    is_it_tuesday(checkme)
