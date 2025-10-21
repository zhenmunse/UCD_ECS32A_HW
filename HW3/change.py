# Homework 3 Part II (change.py)
# Coder: Zonglin Han
# This program simulates best change making.

# Initialization
change = int(input("Enter cents:"))

# Calculate minimum number of coins
quarters = change // 25
dimes = (change % 25) // 10
nickels = (change % 25 % 10) // 5
pennies = change % 5

# Display the result
print(f"The minimum coins for {change} cents are:")
print(f"{quarters} Quarters")
print(f"{dimes} Dimes")
print(f"{nickels} Nickels")
print(f"{pennies} Pennies")