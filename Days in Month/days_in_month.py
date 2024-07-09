def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        # print("Leap year")
        return True
      else:
        # print("Not leap year")
        return False
    else:
      # print("Leap year")
      return True
  else:
    # print("Not leap year")
    return False

def days_in_month(year, month):
  is_leap(year)
  if is_leap(year):
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month - 1]
  else:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    return month_days[month - 1]
  
year = int(input("Enter a year"))
month = int(input("Enter a month"))
days = days_in_month(year, month)
print(days)

