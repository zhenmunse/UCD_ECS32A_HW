# Homework 1 Part VI (heart.py)
# Coder: Zonglin Han
# This program calculates the target heart rate.

# Initialize variables
age = int(input("Enter your age:"))

# Calculate and output the maximum and target heart rate
print("Your maximum heart rate is", 220 - age, "bpm")
print("Your target heart rate is", (220 - age) * 0.5, "-", (220 - age) * 0.85, "bpm")