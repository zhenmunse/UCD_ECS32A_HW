# Homework 1 Part IX (divide.py)
# Coder: Zonglin Han
# This program does whole number division and modulus.

# Initialize variables
number = int(input("Enter a number:"))
divisor = int(input("Enter a number to divide that by:"))

# Calculate and output the quotient and remainder
quotient = number // divisor
remainder = number % divisor
print(number, "divided by", divisor, "is", quotient, "with", remainder, "remaining")