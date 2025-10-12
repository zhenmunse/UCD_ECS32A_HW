# Homework 2 Challenge Problem (approx.py)
# Coder: Zonglin Han
# This program compares two float numbers for approximate equality.

num1 = float(input('Enter a number:'))  # get first float input
num2 = float(input('Enter a number:'))  # get second float input

diff = abs(num1 - num2) # calculate absolute difference

# Check categories
if num1 == num2:
    print("Those numbers are identical")
elif diff < 10**(-9):
    print("Those numbers are very nearly identical")
else:
    # loop through 2 to 9 decimal places
    for n in range(9, 1, -1):  # from 9 down to 2
        if diff < 10**(-n): # check if difference is less than 10^-n
            print(f"Those numbers are the same to {n} decimal places")
            break
    else:
        print("Those numbers are different")