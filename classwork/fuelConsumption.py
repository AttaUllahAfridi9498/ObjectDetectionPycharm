#Description:
# 1 American mile = 1609.344 meters
    # 1 American gallon = 3.785411784 liters
    # Convert liters per 100km to liters per km
# 1 American mile = 1609.344 meters
# 1 American gallon = 3.785411784 liters
# Convert miles per gallon to kilometers per gallon

def liters_100km_to_miles_gallon(liters_per_100km):

    liters_per_km = liters_per_100km / 100
    # Convert liters per km to gallons per km
    gallons_per_km = liters_per_km / 3.785411784
    # Convert gallons per km to miles per km
    miles_per_km = 1 / 1.609344
    # Convert miles per km to miles per gallon
    miles_per_gallon = miles_per_km / gallons_per_km
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles_per_gallon):

    kilometers_per_gallon = miles_per_gallon * 1.609344
    # Convert kilometers per gallon to liters per gallon
    liters_per_gallon = kilometers_per_gallon * 3.785411784
    # Convert liters per gallon to liters per 100km
    liters_per_100km = liters_per_gallon * 100
    return liters_per_100km

# Test data
test_values_liters = [23.5, 12.5, 9.0, 1.5, 3.6]
test_values_miles = [10, 20, 30, 100, 50]

"""
while True:
    choice=int(input("Enter Choice for function call:\n 1. For liters to mile. \n 2. For gallon to liters"))
    if choice==1:
        liters_100km_to_miles_gallon()
        break
    elif choice==2:
        miles_gallon_to_liters_100km()
    else:
        exit()
"""
# Test liters_100km_to_miles_gallon function
for value in test_values_liters:
    print("Test Data of Liters to Miles")
    result = liters_100km_to_miles_gallon(value)
    print(result)

# Test miles_gallon_to_liters_100km function
for value in test_values_miles:
    print("Test Data of Gallon to Liters:")
    result = miles_gallon_to_liters_100km(value)
    print(result)
