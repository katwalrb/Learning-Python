#days in month

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(test_year, test_month):
    """Returns how many days are there in a particular
    month of a particular year."""
    if test_month>12 or test_month<1:
        return "Invalid input."
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    leap_year = is_leap(test_year)
    if is_leap(test_year) == True:
        month_days[1] = 29
    number_of_days = month_days[test_month-1]
    return f"Total days in {test_month}th month of {test_year}: {number_of_days}"
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year,month)
print(days)


