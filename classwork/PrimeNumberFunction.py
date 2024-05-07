def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    # Check divisibility up to half of the number
    for i in range(5, num // 2 + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 10):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
