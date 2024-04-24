# Define the matrix to store temperature readings
temperature_matrix = [[0.0] * 24 for _ in range(31)]
noon_temperature_sum = 0.0
"""

temperature_matrix = [] 
for _ in range(31):
    # Create a new list representing temperature readings for the current day
    # Initialize the list with 24 elements, each initialized to 0.0 (representing the temperature)
    # This list represents 24 hours in a day
    day_temperatures = [0.0] * 24
    temperature_matrix.append(day_temperatures)

"""


# Calculate the monthly average noon temperature

for day_temperatures in temperature_matrix:
    noon_temperature_sum += day_temperatures[12]  # Index 12 represents noon

monthly_average_noon_temperature = noon_temperature_sum / 31

print("Monthly average noon temperature:", monthly_average_noon_temperature)
