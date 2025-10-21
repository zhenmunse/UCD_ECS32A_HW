# Homework 3 Part I (pocket.py)
# Coder: Zonglin Han
# This program runs a pocket change calculator.

# Initialization
print("Compute your pocket change!")
quarter = int(input("Quarters?"))
dime = int(input("Dimes?"))
nickel = int(input("Nickels?"))
penny = int(input("Pennies?"))

# Calculate total amount of change
total = quarter * 0.25 + dime * 0.10 + nickel * 0.05 + penny * 0.01

# Format and display the total amount
print(f"The total is ${total:.2f}")