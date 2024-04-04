n= int(input("Enter a value:"))
steps=0

#def collatz_steps(n):
   # steps = 0
while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
        print(n)
print("Total steps:",steps)
  #  return steps
""""
# Test cases
test_cases = [15, 16, 1023]
for num in test_cases:
    print("Sample input:", num)
    steps = collatz_steps(num)
    print("steps =", steps)
"""