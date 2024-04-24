
temps = []
for d in range(31):
    print("Enter temperature readings for Day", d)
    day_temperatures = []
    for h in range(24):
        temp = float(input(f"Enter temperature for Hour {h + 1}: "))
        day_temperatures.append(temp)
    temps.append(day_temperatures)
hot_days = 0
for day in temps:
    if day[31] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")
