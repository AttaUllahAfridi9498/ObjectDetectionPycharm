
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 == 0) or (year % 400 != 0):
        return True
    else:
        return False


# Test data
test_years = [1900, 2000, 2016, 1987]
expected_results = [False, True, True, False]


# Test the function
for i in range(len(test_years)):
    result = is_leap_year(test_years[i])
    expected_result = expected_results[i]

    if result == expected_result:
        print(f"Test {i + 1}: Ok")
    else:
        print(f"Test {i + 1}: Failed. Expected {expected_result}, but got {result}")
