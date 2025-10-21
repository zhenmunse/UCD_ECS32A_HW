# Homework 3 Part VI (roth.py)
# Coder: Zonglin Han
# This program calculates time to double money in a Roth IRA.

# Initialization
initMoney = float(input("Enter an initial Roth IRA deposit amount:"))
rate = int(input("Enter an annual percent rate of return:"))
initCents = round(initMoney * 100)  # Convert to cents to avoid floating point issues
year = 0
money = initCents

while money < 2 * initCents:    # Loop until money doubles
    interest = money * rate / 100 # Calculate interest for the year
    money += interest # Update total money with interest
    year += 1
    print(f"Value after year {year}: ${money / 100:.2f}")   # Print value after each year

# Output the number of years to double the investment
print(f"It will take {year} years to double your investment with a {rate}% APR.")