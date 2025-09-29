# Homework 1 Part V (bmi.py)
# Coder: Zonglin Han
# This program calculates the Body Mass Index (BMI).

# Initialize variables
height = float(input("Enter height in inches:"))
weight = float(input("Enter weight in pounds:"))

# Calculate BMI
bmi = (weight / (height ** 2)) * 703

# Output the BMI
print("BMI:", bmi)