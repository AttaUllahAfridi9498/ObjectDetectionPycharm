def is_year_leap(year):
    # Leap year is divisible by 4, but not divisible by 100 unless divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(year, month):
    # List of days in each month (1-indexed)
    month_lengths = [31, 28 + is_year_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if month is valid
    if month < 1 or month > 12:
        return None

    # Return number of days for the given month/year pair
    return month_lengths[month - 1]


def day_of_year(year, month, day):
    # Check if year, month, and day are valid
    if year < 1 or month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None

    # Calculate day of the year
    day_of_year = sum(days_in_month(year, m) for m in range(1, month)) + day

    return day_of_year


print(day_of_year(2000, 12, 31))  # Test case

# Additional test cases
additional_test_data = [
    (2023, 1, 1),
    (2024, 2, 29),
    (2022, 4, 15),
    (2022, 6, 30),
    (2022, 9, 31),  # Invalid date (September 31st)
    (2022, 13, 1),  # Invalid month
    (2022, 0, 1),   # Invalid month
    (2022, 1, 0),   # Invalid day
    (2022, 1, 32),  # Invalid day
]
expected_results_additional = [1, 60, 105, 181, None, None, None, None, None]

# Test the function with additional test cases
for i, (year, month, day) in enumerate(additional_test_data):
    result = day_of_year(year, month, day)
    expected_result = expected_results_additional[i]
    if result == expected_result:
        print(f"Year {year}, Month {month}, Day {day}: {result}")
    else:
        print(f"Year {year}, Month {month}, Day {day}: Failed, expected {expected_result}, got {result}")
