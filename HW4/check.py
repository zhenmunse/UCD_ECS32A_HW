# Homework 4 Challenge Problem (check.py)
# Coder: Zonglin Han
# This program validates a credit card number.

num = input("Enter your 8-digit card number:").replace(" ", "") # Prompt user for card number
checkDigit_1 = int(num[7])+int(num[5])+int(num[3])+int(num[1])
checkDigit_2 = 0
for i in [0,2,4,6]: # Indices of digits to be doubled
    double = int(num[i]) * 2
    if double >= 10: # If the doubled value is two digits, sum them with its digits
        double = (double // 10) + (double % 10) 
    checkDigit_2 += double
checkDigit = (checkDigit_1 + checkDigit_2) % 10 # Calculate the check digit
if checkDigit: # If check digit is not zero, it's invalid
    print("Invalid")
    print(f"Check digit should be {(int(num[7]) - checkDigit) % 10}")
else: # If check digit is zero, it's valid
    print("Valid")