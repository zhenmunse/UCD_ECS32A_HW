# Short Topic 1 Random Number Module

------

> “The chains of habit are too weak to be felt until they are too strong to be broken.” – Samuel Johnson

## 1. Random Number Generation

### Random number functions

- For some applications we want unpredictability.
- Truly random numbers are unpredictable.
- Python offers us pseudorandom numbers. They look random,  but are a reproducible result of a complex deterministic (i.e.  predictable) calculation.
- To us they are unpredictable, so we will just call them  random.
- We could use the function `seed()` to initialize the Python  random number generator to create a reproducible sequence  of random numbers.

### Importing the `random` module

A *module* contains importable code. Importing the  random module defines functions that return random  numbers. We can import the module, which was  installed with Python, using the following syntax: 

```python
import random
choice = random.randint(0,20)
```

The import statement creates a module object named  random.

We can use `dir(random)` to see what functions a  module contains after it is imported.

### Generating random numbers

We can assess functions in the random module  using the module dot function syntax.

------

## 2. Random Number Generation

### `random()`

Draw a random floating point between 0 and 1. For example:

```python
import random
random.random() # 0.36243076104854977
```

------

### `randint()`

Draw a random integer within a specified range. For example:

```python
import random
random.randint(1,100) # 59
```

---

### `choice()`

Choose from a sequence of values. For example:

```python
import random
placeList = ["Sycamore", "N Sycamore", "Amtrak", "Downtown", "W Sacramento"]
random.choice(placeList) # One of above
```

------

### `seed()`

 Use only if reproducibility needed. For example:

```python 
import random
random.seed(1)
random.random() # Random Value I
random.random() # Random Value II

random.seed(1) # call seed again
random.random() # Random Value I
```

## 3. Coin Flipping Game

Computer flips a coin and keeps the result hidden from  the user in the variable `coin`.

The coin is represented by the strings `"h"` and `"t"` for  heads and tails given to the random function `choice()`.

The user is asked to guess the outcome. The guess is stored in the variable `guess`. 

```python
import random
coin = random.choice(["h","t"])
guess = input("Guess (h)eads or (t)ails:")
if guess == coin:
    print("You win!")
else:
    print("Bad luck!")
if coin == "h":
    print("It was heads.")
else:
    print("It was tails.")
```

------

## 4. Number Guessing Game

 Computer randomly picks the number 1, 2, or 3 to "think" about while the user makes a guess.

We use the random function `randint()` to choose the number and store it in the variable `pick`.

```python
pick = random.randint(1,3)
```

The user is asked to guess the outcome. The guess is stored in the variable `guess`.

```python
guess = int(input("Enter your guess:"))
```

In total:

```python
 import random
 pick = random.randint(1,3)
 print("I'm thinking of a number between 1 and 3.")
 guess = int(input("Enter your guess:"))
 if guess == pick:
    print("You're right!")
 elif guess < pick:
    print("Too low!")
 else:
    print("Too high!")
 print("I was thinking of " + str(pick) + ".")
```
