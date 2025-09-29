# Homework 1 Part VIII (circle.py)
# Coder: Zonglin Han
# This program calculates the properties of a circle.

# Initialize variables
radius = float(input("Enter radius:"))
pi = 3.14159

# Calculate and output the diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius**2

print("Diameter", diameter)
print("Circumference", circumference)
print("Area", area)