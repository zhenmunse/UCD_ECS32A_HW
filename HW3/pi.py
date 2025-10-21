# Homework 3 Challenge Problem (pi.py)
# Coder: Zonglin Han
# This program approximates the value of pi.

import math # Import math module for accurate pi value

# Initialization
numberOfTerms = int(input("Number of terms:"))
pi = 0.0
sign = 1
denominator = 1.0

# Calculate pi
count = 0
while count < numberOfTerms:    # Loop for the specified number of terms
    pi += sign * 4.0 / denominator
    sign *= -1 # Alternate the sign
    denominator += 2
    count += 1

# Output the results
print(f"Estimate of pi: {pi:.9f}")
print(f"Error: {math.pi-pi:.9f}")