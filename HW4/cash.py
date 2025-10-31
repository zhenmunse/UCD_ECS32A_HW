# Homework 4 Part VIII (cash.py)
# Coder: Zonglin Han
# This program simulates a cash register that calculates total cost.

print("Automated cash register")
total = 0.0
count = 0
fileName = input("Enter file of prices:")
with open(fileName, 'r') as file: # Open the file containing prices
    for line in file:
        line = line.strip()
        if line == "":  # Skip empty lines
            continue
        price = float(line) # Convert each line to a float
        total += price # Add the price to the total
        count += 1
print(f"File contained {count} items totaling ${total:.2f}") # Print the total number of items and total cost