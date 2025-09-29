# Homework 1 Part VII (paint.py)
# Coder: Zonglin Han
# This program calculates the amount of paint needed to paint a room.

print("Paint coverage estimator") # Print the title

# Initialize variables
length = float(input("Length of room in inches:"))
width = float(input("Width of room in inches:"))
height = float(input("Average height of room in inches:"))


# Calculate and output the amount of paint needed
area = 2 * (length * height + width * height) / (12**2) # Convert to square feet
paint_needed = int(area / 100) + 1
print("You'll want", paint_needed, "cans.")