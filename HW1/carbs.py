# Homework 1 Part X (carbs.py)
# Coder: Zonglin Han
# This program calculates the percentage of calories obtained from carbohydrates.

# Initialize variables
item=input("Enter menu item:")
calories=int(input("Enter calories:"))
carbs=int(input("Enter carbs in grams:"))

# Calculation
carb_cals = carbs * 4
percent_carb = (carb_cals / calories) * 100
calories_rounded = round(calories, -1)       # round to 10s place
percent_carb_rounded = round(percent_carb)   # round to nearest integer
percent_str = str(percent_carb_rounded)+"%"

print(item,calories_rounded,"Cals",percent_str,"Carbs")