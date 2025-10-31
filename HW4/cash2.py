# Homework 4 Part IX (cash2.py)
# Coder: Zonglin Han
# This program simulates a SMART cash register that calculates total cost.

print("Automated cash register")
total = 0.0
count = 0
fileName = input("Enter file of prices:")
with open(fileName, 'r') as file: # Open the file containing prices
    for line in file:
        line = line.strip("$ \n\t")
        try:
            price = float(line) # Convert each line to a float
            total += price # Add the price to the total
            count += 1
        except ValueError:  # Handle invalid price format
            continue

print(f"File contained {count} items totaling ${total:.2f}") # Print the total number of items and total cost