# Homework 3 Part IV (tip.py)
# Coder: Zonglin Han
# This program generates tip table.

# Initialization
total = float(input("Enter total:"))

tip_rate = 15
while tip_rate <= 25:   # Generate tips from 15% to 25%
    tip = total * tip_rate / 100
    print(f"A {tip_rate}% tip is ${tip:.2f}") # Display tip amount
    tip_rate += 1