def is_prime(number):
    # Check if number is less than 2
    if number < 2:
        return False

    # Check for divisors from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

# Test data
test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected results
expected_results = [False, True, True, False, True, False, True, False, False, False]

# Test the function
for i, number in enumerate(test_numbers):
    result = is_prime(number)
    expected_result = expected_results[i]
    if result == expected_result:
        print(f"Number {number}: Passed")
    else:
        print(f"Number {number}: Failed, expected {expected_result}, got {result}")
