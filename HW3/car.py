# Homework 3 Part VII (car.py)
# Coder: Zonglin Han
# This program guesses the car price.

# Initialization
price = 44500
time = 0
print("Guess the price and win the prize!")

while True: # Infinite loop for guessing
    guess = int(input("Enter your guess:"))
    time += 1
    if guess > price: # Check if the guess is too high
        print("Too high!")
    elif guess < price: # Check if the guess is too low
        print("Too low!")
    else: # Correct guess
        print(f"It took {time} guesses.")
        break

# Check if the user won within 5 guesses
if time <= 5:
    print("You won the car!")
else:
    print("Too many guesses!")