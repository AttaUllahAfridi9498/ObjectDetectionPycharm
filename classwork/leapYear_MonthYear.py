def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    # List containing the number of days for each month (January to December)
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if the arguments make sense
    if month < 1 or month > 12 or year < 1:
        return None

    # Check if it's a leap year and adjust February's length accordingly
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28

    # Return the number of days for the given month/year pair
    return month_lengths[month - 1]


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print(result)
    else:
        print("Failed")
