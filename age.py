from datetime import datetime as dt

#This function takes the date inputted by the user and converts it
#To a datetime library compatible date
def date_converter(date):
  new_date = dt.strptime(date,"%d-%m-%Y")
  return new_date

#This function calculates the age of the person using datetime.timedelta
def age_calculator(date):
  today = dt.today()
  delta = today - date
  years = int(delta.days/365.25)
  print(years)
  pass

#Main block of code that calls the functions to be used
if __name__ == "__main__":
  date = input("Please enter a date (dd-mm-yyyy): ")
  new_date = date_converter(date)
  age_calculator(new_date)