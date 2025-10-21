# Homework 3 Part VIII (mileage.py)
# Coder: Zonglin Han
# This program calculates personal fuel economy.

# Initialization
miles = 0
gallons = 0
print("Your Personal Fuel Economy")
while True: # Infinite loop for input
    travelDistance = input("Number of miles traveled (or enter to exit):")
    if travelDistance == "": # Exit condition
        break
    miles += int(travelDistance) # Accumulate miles
    travelFuel = float(input("Number of gallons needed:"))
    gallons += travelFuel # Accumulate gallons
    print(f"Mileage this tank = {int(travelDistance) / int(travelFuel):.1f}")

# Final average mileage calculation
print(f"Average mileage = {miles / gallons:.1f}")