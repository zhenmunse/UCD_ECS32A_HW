# Homework 4 Part III (phone.py)
# Coder: Zonglin Han
# This program validates phone numbers.

num = input("Enter number as ### ###-####:")    # Prompt user for phone number
if (len(num) == 12  # Check length
    and all(c.isdigit() for c in num[0:3]) # Check first three digits
    and num[3] == ' ' # Check space
    and all(c.isdigit() for c in num[4:7]) # Check next three digits
    and num[7] == '-' # Check hyphen
    and all(c.isdigit() for c in num[8:12])): # Check last four digits
    print("Valid")
else:   # If any of the checks fail
    print("Invalid")
