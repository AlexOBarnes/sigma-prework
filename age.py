from datetime import datetime as dt

def date_converter(date):
  new_date = dt.strptime(date,"%d-%m-%Y")
  return new_date

def age_calculator(date):
  today = dt.today()
  delta = today - date
  years = int(delta.days/365.25)
  print(years)
  pass

if __name__ == "__main__":
  date = input("Please enter a date (dd-mm-yyyy): ")
  new_date = date_converter(date)
  age_calculator(new_date)