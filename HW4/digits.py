# Homework 4 Part IV (digits.py)
# Coder: Zonglin Han
# This program extracts phone number from a given string.

num = ""
raw_input = input("Enter phone number:") # Prompt user for input string
for i in raw_input:
    if i.isdigit(): # Check if the character is a digit
        num += i
print(f"Digit string: {num}") # Print the extracted digit string