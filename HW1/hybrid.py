# Homework 1 Challenge Problem (hybrid.py)
# Coder: Zonglin Han
# This program calculates the cost of owning a Hybrid Car

# Initialize variables
cost = int(input("Cost of car:"))
miles_per_year = int(input("Miles driven per year:"))
cost_of_gas = float(input("Cost of gas:"))
mpg = int(input("Fuel efficiency (mpg):"))
estimated_resale = int(input("Estimated resale value after 5 years:"))

# Calculate costs
five_year_gas_cost = float((miles_per_year * 5 / mpg) * cost_of_gas)
five_year_car_cost = float(cost - estimated_resale)

# Print results
print("Five year gas cost:", five_year_gas_cost)
print("Five year car cost:", five_year_car_cost)
print("Five year total cost:", five_year_gas_cost + five_year_car_cost)