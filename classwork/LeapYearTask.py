def is_leap_year(year):
    if year % 4 != 0:
        # print("Common year")
        return False
        # Check if the year is divisible by 100
    elif year % 100 != 0:
        # print("Leap year")
        return True
        # Check if the year is divisible by 400
    elif year % 400 == 0:
        # print("Common year")
        return False
    else:
        # print("Leap year")
        return False
    #return (year % 4 != 0 and year % 100 != 0) or (year % 400 == 0)
    #return (year%4==0 and year%100!=0) or (year%400==0)
    """
    if year%4==0 and year%100!=0:
        return True
    elif year%400==0:
        return True
    else:
        return False
    """


# Test data and expected results
test_data = [1900, 2000, 2016, 1987]
expected_results = [False, True, True, False]

for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_leap_year(yr)
	if result == expected_results[i]:
		print("True")
	else:
		print("False")
