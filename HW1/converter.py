# Homework 1 Part XI (converter.py)
# Coder: Zonglin Han
# This program converts letter to integer and binary expressions

# Initialize variables
character = input("Enter a character:")
num = ord(character)  # get ASCII value
binary = bin(num)    # convert to binary

print(character,"corresponds to the integer", num, "which is",binary,"in binary.")
