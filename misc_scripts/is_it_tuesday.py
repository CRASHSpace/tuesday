import datetime

date = datetime.datetime.today()

def is_it_tuesday(date_to_check):
  if date_to_check.weekday() == 1:
    print("yes")
  else:
    print("no")

if __name__ == "__main__":
  is_it_tuesday(date)
