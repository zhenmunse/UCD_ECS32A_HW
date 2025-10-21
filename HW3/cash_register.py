# Homework 3 Part V (cash_register.py)
# Coder: Zonglin Han
# This program simulates a cash register.

# Initialization
print("Cash register (press enter to exit)")

# Variables to track total cost and item count
total_cost = 0.0
count = 0

# Loop to get item costs
while True:
    item_cost = (input("Enter item cost:"))
    if item_cost == "":
        break
    total_cost += float(item_cost)
    count += 1

# Display the total number of items and total cost
print(f"You entered {count} items totaling ${total_cost:.2f}")